u"""
AllenNLP just uses
`PyTorch optimizers <http://pytorch.org/docs/master/optim.html>`_ ,
with a thin wrapper to allow registering them and instantiating them ``from_params``.

The available optimizers are

* `"adadelta" <http://pytorch.org/docs/master/optim.html#torch.optim.Adadelta>`_
* `"adagrad" <http://pytorch.org/docs/master/optim.html#torch.optim.Adagrad>`_
* `"adam" <http://pytorch.org/docs/master/optim.html#torch.optim.Adam>`_
* `"sparse_adam" <http://pytorch.org/docs/master/optim.html#torch.optim.SparseAdam>`_
* `"sgd" <http://pytorch.org/docs/master/optim.html#torch.optim.SGD>`_
* `"rmsprop <http://pytorch.org/docs/master/optim.html#torch.optim.RMSprop>`_
* `"adamax <http://pytorch.org/docs/master/optim.html#torch.optim.Adamax>`_
* `"averaged_sgd <http://pytorch.org/docs/master/optim.html#torch.optim.ASGD>`_
"""



from __future__ import division
from __future__ import absolute_import
import logging
import re
import math
#typing

import torch

from allennlp.common import Params, Registrable

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class Optimizer(Registrable):
    u"""
    This class just allows us to implement ``Registrable`` for Pytorch Optimizers.
    """
    default_implementation = u"adam"

    # Requires custom from_params.
    @classmethod
    def from_params(cls, model_parameters      , params        ):  # type: ignore
        # pylint: disable=arguments-differ
        if isinstance(params, unicode):
            optimizer = params
            params = Params({})
        else:
            optimizer = params.pop_choice(u"type", Optimizer.list_available())

        # make the parameter groups if need
        groups = params.pop(u"parameter_groups", None)
        if groups:
            # The input to the optimizer is list of dict.
            # Each dict contains a "parameter group" and groups specific options,
            # e.g., {'params': [list of parameters], 'lr': 1e-3, ...}
            # Any config option not specified in the additional options (e.g.
            # for the default group) is inherited from the top level config.
            # see: http://pytorch.org/docs/0.3.0/optim.html?#per-parameter-options
            #
            # groups contains something like:
            #"parameter_groups": [
            #       [["regex1", "regex2"], {"lr": 1e-3},
            #        ["regex3"], {"lr": 1e-4}]
            #]
            #(note that the allennlp config files require double quotes ", and will
            # fail (sometimes silently) with single quotes ').

            # This is typed as as Any since the dict values other then
            # the params key are passed to the Optimizer constructor and
            # can be any type it accepts.
            # In addition to any parameters that match group specific regex,
            # we also need a group for the remaining "default" group.
            # Those will be included in the last entry of parameter_groups.
            parameter_groups      = [{u'params': []} for _ in range(len(groups) + 1)]
            # add the group specific kwargs
            for k in range(len(groups)): # pylint: disable=consider-using-enumerate
                parameter_groups[k].update(groups[k][1].as_dict())

            regex_use_counts                 = {}
            parameter_group_names            = [set() for _ in range(len(groups) + 1)]
            for name, param in model_parameters:
                # Determine the group for this parameter.
                group_index = None
                for k, group_regexes in enumerate(groups):
                    for regex in group_regexes[0]:
                        if regex not in regex_use_counts:
                            regex_use_counts[regex] = 0
                        if re.search(regex, name):
                            if group_index is not None and group_index != k:
                                raise ValueError(u"{} was specified in two separate parameter groups".format(name))
                            group_index = k
                            regex_use_counts[regex] += 1

                if group_index is not None:
                    parameter_groups[group_index][u'params'].append(param)
                    parameter_group_names[group_index].add(name)
                else:
                    # the default group
                    parameter_groups[-1][u'params'].append(param)
                    parameter_group_names[-1].add(name)

            # log the parameter groups
            logger.info(u"Done constructing parameter groups.")
            for k in range(len(groups) + 1):
                group_options = dict((key, val) for key, val in list(parameter_groups[k].items())
                                 if key != u'params')
                logger.info(u"Group %s: %s, %s", k,
                            list(parameter_group_names[k]),
                            group_options)
            # check for unused regex
            for regex, count in list(regex_use_counts.items()):
                if count == 0:
                    logger.warning(u"When constructing parameter groups, "
                                   u" %s not match any parameter name", regex)

        else:
            parameter_groups = [param for name, param in model_parameters]

        # Log the number of parameters to optimize
        num_parameters = 0
        for parameter_group in parameter_groups:
            if isinstance(parameter_group, dict):
                num_parameters += sum(parameter.numel() for parameter in parameter_group[u"params"])
            else:
                num_parameters += parameter_group.numel()
        logger.info(u"Number of trainable parameters: %s", num_parameters)
        return Optimizer.by_name(optimizer)(parameter_groups, **params.as_dict()) # type: ignore

# We just use the Pytorch optimizers, so here we force them into
# Registry._registry so we can build them from params.
Registrable._registry[Optimizer] = {   # pylint: disable=protected-access
        u"adam": torch.optim.Adam,
        u"sparse_adam": torch.optim.SparseAdam,
        u"adagrad": torch.optim.Adagrad,
        u"adadelta": torch.optim.Adadelta,
        u"sgd": torch.optim.SGD,
        u"rmsprop": torch.optim.RMSprop,
        u"adamax": torch.optim.Adamax,
        u"averaged_sgd": torch.optim.ASGD,
}



class DenseSparseAdam(torch.optim.Optimizer):
    # pylint: disable=protected-access,cell-var-from-loop
    # pylint: disable=unneeded-not,misplaced-comparison-constant
    # pylint: disable=len-as-condition,invalid-name,anomalous-backslash-in-string
    u"""
    NOTE: This class has been copied verbatim from the separate Dense and
    Sparse versions of Adam in Pytorch.

    Implements Adam algorithm with dense & sparse gradients.
    It has been proposed in Adam: A Method for Stochastic Optimization.

    Parameters
    ----------
    params : ``iterable``
        iterable of parameters to optimize or dicts defining parameter groups
    lr : ``float``, optional (default: 1e-3)
        The learning rate.
    betas : ``Tuple[float, float]``, optional (default: (0.9, 0.999))
        coefficients used for computing running averages of gradient
        and its square.
    eps : ``float``, optional, (default: 1e-8)
        A term added to the denominator to improve numerical stability.
    """
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8):
        if not 0.0 <= lr:
            raise ValueError(u"Invalid learning rate: {}".format(lr))
        if not 0.0 <= eps:
            raise ValueError(u"Invalid epsilon value: {}".format(eps))
        if not 0.0 <= betas[0] < 1.0:
            raise ValueError(u"Invalid beta parameter at index 0: {}".format(betas[0]))
        if not 0.0 <= betas[1] < 1.0:
            raise ValueError(u"Invalid beta parameter at index 1: {}".format(betas[1]))
        defaults = dict(lr=lr, betas=betas, eps=eps)
        super(DenseSparseAdam, self).__init__(params, defaults)

    def step(self, closure=None):
        u"""
        Performs a single optimization step.

        Parameters
        ----------
        closure : ``callable``, optional.
            A closure that reevaluates the model and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:
            for p in group[u'params']:
                if p.grad is None:
                    continue
                grad = p.grad.data

                state = self.state[p]

                # State initialization
                if len(state) == 0:
                    state[u'step'] = 0
                    # Exponential moving average of gradient values
                    state[u'exp_avg'] = torch.zeros_like(p.data)
                    # Exponential moving average of squared gradient values
                    state[u'exp_avg_sq'] = torch.zeros_like(p.data)

                state[u'step'] += 1

                exp_avg, exp_avg_sq = state[u'exp_avg'], state[u'exp_avg_sq']
                beta1, beta2 = group[u'betas']

                if grad.is_sparse:
                    grad = grad.coalesce()  # the update is non-linear so indices must be unique
                    grad_indices = grad._indices()
                    grad_values = grad._values()
                    size = grad.size()

                    def make_sparse(values):
                        constructor = grad.new
                        if grad_indices.dim() == 0 or values.dim() == 0:
                            return constructor().resize_as_(grad)
                        return constructor(grad_indices, values, size)

                    # Decay the first and second moment running average coefficient
                    #      old <- b * old + (1 - b) * new
                    # <==> old += (1 - b) * (new - old)
                    old_exp_avg_values = exp_avg._sparse_mask(grad)._values()
                    exp_avg_update_values = grad_values.sub(old_exp_avg_values).mul_(1 - beta1)
                    exp_avg.add_(make_sparse(exp_avg_update_values))
                    old_exp_avg_sq_values = exp_avg_sq._sparse_mask(grad)._values()
                    exp_avg_sq_update_values = grad_values.pow(2).sub_(old_exp_avg_sq_values).mul_(1 - beta2)
                    exp_avg_sq.add_(make_sparse(exp_avg_sq_update_values))

                    # Dense addition again is intended, avoiding another _sparse_mask
                    numer = exp_avg_update_values.add_(old_exp_avg_values)
                    exp_avg_sq_update_values.add_(old_exp_avg_sq_values)
                    denom = exp_avg_sq_update_values.sqrt_().add_(group[u'eps'])
                    del exp_avg_update_values, exp_avg_sq_update_values

                    bias_correction1 = 1 - beta1 ** state[u'step']
                    bias_correction2 = 1 - beta2 ** state[u'step']
                    step_size = group[u'lr'] * math.sqrt(bias_correction2) / bias_correction1

                    p.data.add_(make_sparse(-step_size * numer.div_(denom)))

                else:
                    # Decay the first and second moment running average coefficient
                    exp_avg.mul_(beta1).add_(1 - beta1, grad)
                    exp_avg_sq.mul_(beta2).addcmul_(1 - beta2, grad, grad)
                    denom = exp_avg_sq.sqrt().add_(group[u'eps'])

                    bias_correction1 = 1 - beta1 ** state[u'step']
                    bias_correction2 = 1 - beta2 ** state[u'step']
                    step_size = group[u'lr'] * math.sqrt(bias_correction2) / bias_correction1

                    p.data.addcdiv_(-step_size, exp_avg, denom)

        return loss

DenseSparseAdam = Optimizer.register(u'dense_sparse_adam')(DenseSparseAdam)
