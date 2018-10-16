"""Target generators for YOLOs."""
# pylint: disable=arguments-differ, unsupported-assignment-operation
from __future__ import absolute_import
from __future__ import division

import numpy as np
from mxnet import gluon
from mxnet import nd
from mxnet import autograd
from ...nn.bbox import BBoxCornerToCenter, BBoxCenterToCorner, BBoxBatchIOU


class YOLOV3PrefetchTargetGenerator(gluon.Block):
    """YOLO V3 prefetch target generator.
    The target generated by this instance is invariant to network predictions.
    Therefore it is usually used in DataLoader transform function to reduce the load on GPUs.

    Parameters
    ----------
    num_class : int
        Number of foreground classes.

    """
    def __init__(self, num_class, **kwargs):
        super(YOLOV3PrefetchTargetGenerator, self).__init__(**kwargs)
        self._num_class = num_class
        self.bbox2center = BBoxCornerToCenter(axis=-1, split=True)
        self.bbox2corner = BBoxCenterToCorner(axis=-1, split=False)


    def forward(self, img, xs, anchors, offsets, gt_boxes, gt_ids, gt_mixratio=None):
        """Generating training targets that do not require network predictions.

        Parameters
        ----------
        img : mxnet.nd.NDArray
            Original image tensor.
        xs : list of mxnet.nd.NDArray
            List of feature maps.
        anchors : mxnet.nd.NDArray
            YOLO3 anchors.
        offsets : mxnet.nd.NDArray
            Pre-generated x and y offsets for YOLO3.
        gt_boxes : mxnet.nd.NDArray
            Ground-truth boxes.
        gt_ids : mxnet.nd.NDArray
            Ground-truth IDs.
        gt_mixratio : mxnet.nd.NDArray, optional
            Mixup ratio from 0 to 1.

        Returns
        -------
        (tuple of) mxnet.nd.NDArray
            objectness: 0 for negative, 1 for positive, -1 for ignore.
            center_targets: regression target for center x and y.
            scale_targets: regression target for scale x and y.
            weights: element-wise gradient weights for center_targets and scale_targets.
            class_targets: a one-hot vector for classification.

        """
        assert isinstance(anchors, (list, tuple))
        all_anchors = nd.concat(*[a.reshape(-1, 2) for a in anchors], dim=0)
        assert isinstance(offsets, (list, tuple))
        all_offsets = nd.concat(*[o.reshape(-1, 2) for o in offsets], dim=0)
        num_anchors = np.cumsum([a.size // 2 for a in anchors])
        num_offsets = np.cumsum([o.size // 2 for o in offsets])
        _offsets = [0] + num_offsets.tolist()
        assert isinstance(xs, (list, tuple))
        assert len(xs) == len(anchors) == len(offsets)

        # orig image size
        orig_height = img.shape[2]
        orig_width = img.shape[3]
        with autograd.pause():
            # outputs
            shape_like = all_anchors.reshape((1, -1, 2)) * all_offsets.reshape(
                (-1, 1, 2)).expand_dims(0).repeat(repeats=gt_ids.shape[0], axis=0)
            center_targets = nd.zeros_like(shape_like)
            scale_targets = nd.zeros_like(center_targets)
            weights = nd.zeros_like(center_targets)
            objectness = nd.zeros_like(weights.split(axis=-1, num_outputs=2)[0])
            class_targets = nd.one_hot(objectness.squeeze(axis=-1), depth=self._num_class)
            class_targets[:] = -1  # prefill -1 for ignores

            # for each ground-truth, find the best matching anchor within the particular grid
            # for instance, center of object 1 reside in grid (3, 4) in (16, 16) feature map
            # then only the anchor in (3, 4) is going to be matched
            gtx, gty, gtw, gth = self.bbox2center(gt_boxes)
            shift_gt_boxes = nd.concat(-0.5 * gtw, -0.5 * gth, 0.5 * gtw, 0.5 * gth, dim=-1)
            anchor_boxes = nd.concat(0 * all_anchors, all_anchors, dim=-1)  # zero center anchors
            shift_anchor_boxes = self.bbox2corner(anchor_boxes)
            ious = nd.contrib.box_iou(shift_anchor_boxes, shift_gt_boxes).transpose((1, 0, 2))
            # real value is required to process, convert to Numpy
            matches = ious.argmax(axis=1).asnumpy()  # (B, M)
            valid_gts = (gt_boxes >= 0).asnumpy().prod(axis=-1)  # (B, M)
            np_gtx, np_gty, np_gtw, np_gth = [x.asnumpy() for x in [gtx, gty, gtw, gth]]
            np_anchors = all_anchors.asnumpy()
            np_gt_ids = gt_ids.asnumpy()
            np_gt_mixratios = gt_mixratio.asnumpy() if gt_mixratio is not None else None
            # TODO(zhreshold): the number of valid gt is not a big number, therefore for loop
            # should not be a problem right now. Switch to better solution is needed.
            for b in range(matches.shape[0]):
                for m in range(matches.shape[1]):
                    if valid_gts[b, m] < 1:
                        break
                    match = int(matches[b, m])
                    nlayer = np.nonzero(num_anchors > match)[0][0]
                    height = xs[nlayer].shape[2]
                    width = xs[nlayer].shape[3]
                    gtx, gty, gtw, gth = (np_gtx[b, m, 0], np_gty[b, m, 0],
                                          np_gtw[b, m, 0], np_gth[b, m, 0])
                    # compute the location of the gt centers
                    loc_x = int(gtx / orig_width * width)
                    loc_y = int(gty / orig_height * height)
                    # write back to targets
                    index = _offsets[nlayer] + loc_y * width + loc_x
                    center_targets[b, index, match, 0] = gtx / orig_width * width - loc_x  # tx
                    center_targets[b, index, match, 1] = gty / orig_height * height - loc_y  # ty
                    scale_targets[b, index, match, 0] = np.log(gtw / np_anchors[match, 0])
                    scale_targets[b, index, match, 1] = np.log(gth / np_anchors[match, 1])
                    weights[b, index, match, :] = 2.0 - gtw * gth / orig_width / orig_height
                    objectness[b, index, match, 0] = (
                        np_gt_mixratios[b, m, 0] if np_gt_mixratios is not None else 1)
                    class_targets[b, index, match, :] = 0
                    class_targets[b, index, match, int(np_gt_ids[b, m, 0])] = 1
            # since some stages won't see partial anchors, so we have to slice the correct targets
            objectness = self._slice(objectness, num_anchors, num_offsets)
            center_targets = self._slice(center_targets, num_anchors, num_offsets)
            scale_targets = self._slice(scale_targets, num_anchors, num_offsets)
            weights = self._slice(weights, num_anchors, num_offsets)
            class_targets = self._slice(class_targets, num_anchors, num_offsets)
        return objectness, center_targets, scale_targets, weights, class_targets

    def _slice(self, x, num_anchors, num_offsets):
        """since some stages won't see partial anchors, so we have to slice the correct targets"""
        # x with shape (B, N, A, 1 or 2)
        anchors = [0] + num_anchors.tolist()
        offsets = [0] + num_offsets.tolist()
        ret = []
        for i in range(len(num_anchors)):
            y = x[:, offsets[i]:offsets[i+1], anchors[i]:anchors[i+1], :]
            ret.append(y.reshape((0, -3, -1)))
        return nd.concat(*ret, dim=1)


class YOLOV3DynamicTargetGeneratorSimple(gluon.HybridBlock):
    """YOLOV3 target generator that requires network predictions.
    `Dynamic` indicate that the targets generated depend on current network.
    `Simple` indicate that it only support `pos_iou_thresh` >= 1.0,
    otherwise it's a lot more complicated and slower.
    (box regression targets and class targets are not necessary when `pos_iou_thresh` >= 1.0)

    Parameters
    ----------
    num_class : int
        Number of foreground classes.
    ignore_iou_thresh : float
        Anchors that has IOU in `range(ignore_iou_thresh, pos_iou_thresh)` don't get
        penalized of objectness score.

    """
    def __init__(self, num_class, ignore_iou_thresh, **kwargs):
        super(YOLOV3DynamicTargetGeneratorSimple, self).__init__(**kwargs)
        self._num_class = num_class
        self._ignore_iou_thresh = ignore_iou_thresh
        self._batch_iou = BBoxBatchIOU()

    def hybrid_forward(self, F, box_preds, gt_boxes):
        """Short summary.

        Parameters
        ----------
        F : mxnet.nd or mxnet.sym
            `F` is mxnet.sym if hybridized or mxnet.nd if not.
        box_preds : mxnet.nd.NDArray
            Predicted bounding boxes.
        gt_boxes : mxnet.nd.NDArray
            Ground-truth bounding boxes.

        Returns
        -------
        (tuple of) mxnet.nd.NDArray
            objectness: 0 for negative, 1 for positive, -1 for ignore.
            center_targets: regression target for center x and y.
            scale_targets: regression target for scale x and y.
            weights: element-wise gradient weights for center_targets and scale_targets.
            class_targets: a one-hot vector for classification.

        """
        with autograd.pause():
            box_preds = box_preds.reshape((0, -1, 4))
            objness_t = F.zeros_like(box_preds.slice_axis(axis=-1, begin=0, end=1))
            center_t = F.zeros_like(box_preds.slice_axis(axis=-1, begin=0, end=2))
            scale_t = F.zeros_like(box_preds.slice_axis(axis=-1, begin=0, end=2))
            weight_t = F.zeros_like(box_preds.slice_axis(axis=-1, begin=0, end=2))
            class_t = F.ones_like(objness_t.tile(reps=(self._num_class))) * -1
            batch_ious = self._batch_iou(box_preds, gt_boxes)  # (B, N, M)
            ious_max = batch_ious.max(axis=-1, keepdims=True)  # (B, N, 1)
            objness_t = (ious_max > self._ignore_iou_thresh) * -1  # use -1 for ignored
        return objness_t, center_t, scale_t, weight_t, class_t


class YOLOV3TargetMerger(gluon.HybridBlock):
    """YOLOV3 target merger that merges the prefetched targets and dynamic targets.

    Parameters
    ----------
    num_class : int
        Number of foreground classes.
    ignore_iou_thresh : float
        Anchors that has IOU in `range(ignore_iou_thresh, pos_iou_thresh)` don't get
        penalized of objectness score.

    """
    def __init__(self, num_class, ignore_iou_thresh, **kwargs):
        super(YOLOV3TargetMerger, self).__init__(**kwargs)
        self._num_class = num_class
        self._dynamic_target = YOLOV3DynamicTargetGeneratorSimple(num_class, ignore_iou_thresh)
        self._label_smooth = False

    def hybrid_forward(self, F, box_preds, gt_boxes, obj_t, centers_t, scales_t, weights_t, clas_t):
        """Short summary.

        Parameters
        ----------
        F : mxnet.nd or mxnet.sym
            `F` is mxnet.sym if hybridized or mxnet.nd if not.
        box_preds : mxnet.nd.NDArray
            Predicted bounding boxes.
        gt_boxes : mxnet.nd.NDArray
            Ground-truth bounding boxes.
        obj_t : mxnet.nd.NDArray
            Prefetched Objectness targets.
        centers_t : mxnet.nd.NDArray
            Prefetched regression target for center x and y.
        scales_t : mxnet.nd.NDArray
            Prefetched regression target for scale x and y.
        weights_t : mxnet.nd.NDArray
            Prefetched element-wise gradient weights for center_targets and scale_targets.
        clas_t : mxnet.nd.NDArray
            Prefetched one-hot vector for classification.

        Returns
        -------
        (tuple of) mxnet.nd.NDArray
            objectness: 0 for negative, 1 for positive, -1 for ignore.
            center_targets: regression target for center x and y.
            scale_targets: regression target for scale x and y.
            weights: element-wise gradient weights for center_targets and scale_targets.
            class_targets: a one-hot vector for classification.

        """
        with autograd.pause():
            dynamic_t = self._dynamic_target(box_preds, gt_boxes)
            # use fixed target to override dynamic targets
            obj, centers, scales, weights, clas = zip(
                dynamic_t, [obj_t, centers_t, scales_t, weights_t, clas_t])
            mask = obj[1] > 0
            objectness = F.where(mask, obj[1], obj[0])
            mask2 = mask.tile(reps=(2,))
            center_targets = F.where(mask2, centers[1], centers[0])
            scale_targets = F.where(mask2, scales[1], scales[0])
            weights = F.where(mask2, weights[1], weights[0])
            mask3 = mask.tile(reps=(self._num_class,))
            class_targets = F.where(mask3, clas[1], clas[0])
            smooth_weight = 1. / self._num_class
            if self._label_smooth:
                smooth_weight = 1. / self._num_class
                class_targets = F.where(
                    class_targets > 0.5, class_targets - smooth_weight, class_targets)
                class_targets = F.where(
                    class_targets < -0.5, class_targets, F.ones_like(class_targets) * smooth_weight)
            class_mask = mask.tile(reps=(self._num_class,)) * (class_targets >= 0)
            return [F.stop_gradient(x) for x in [objectness, center_targets, scale_targets,
                                                 weights, class_targets, class_mask]]
