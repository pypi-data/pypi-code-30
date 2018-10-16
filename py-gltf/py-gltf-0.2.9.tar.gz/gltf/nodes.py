import copy
import logging
from enum import Enum

import numpy as np
from PIL import Image as PImage
from pyquaternion import Quaternion

from .utils import BaseGLTFStructure
from .materials import Material, Sampler
from .buffers import Vec3Array, Vec2Array, Vec4Array, ScalarArray

logger = logging.getLogger(__name__)


class Primitive(BaseGLTFStructure):
    _positions = None
    _normals = None
    _texcoords = None
    _indices = None
    _tangents = None
    mode = None
    material = None
    joints = None
    weights = None

    class Mode(Enum):
        POINTS = 0
        LINES = 1
        LINE_LOOP = 2
        LINE_STRIP = 3
        TRIANGLES = 4
        TRIANGLE_STRIP = 5
        TRIANGLE_FAN = 6

    def __init__(self, prim=None, gltf=None, name=None, joints=None, weights=None,
                 positions=None, normals=None, indices=None, texcoords=None, tangents=None,
                 material=None, image=None, texture=None, mode=None):
        self.name = name
        if prim:
            if 'name' in prim:
                self.name = name
            if 'material' in prim:
                self.material = gltf.materials[prim.get('material')]
            if 'indices' in prim:
                self.indices = gltf.accessors[prim.get('indices')]
            if 'mode' in prim:
                self.mode = self.Mode(prim.get('mode'))
            attributes = prim.get('attributes')
            if attributes:
                if 'POSITION' in attributes:
                    self.positions = gltf.accessors[attributes.get('POSITION')]
                if 'NORMAL' in attributes:
                    self.normals = gltf.accessors[attributes.get('NORMAL')]
                if 'TANGENT' in attributes:
                    self.tangents = gltf.accessors[attributes.get('TANGENT')]
                if 'TEXCOORD_0' in attributes:
                    self.texcoords = gltf.accessors[attributes.get('TEXCOORD_0')]
                self.joints = []
                if 'JOINTS_0' in attributes:
                    i = 0
                    while True:
                        joints = attributes.get('JOINTS_' + str(i))
                        if joints is None:
                            break
                        self.joints.append(gltf.accessors[joints])
                        i += 1
                self.weights = []
                if 'WEIGHTS_0' in attributes:
                    i = 0
                    while True:
                        weights = attributes.get('WEIGHTS_' + str(i))
                        if weights is None:
                            break
                        self.weights.append(gltf.accessors[weights])
                        i += 1
        else:
            self.positions = positions
            self.normals = normals
            self.indices = indices
            self.tangents = tangents
            self.texcoords = texcoords
            self.material = material
            self.joints = joints if joints is not None else []
            self.weights = weights if weights is not None else []
            self.mode = mode and self.Mode[mode]
            if image:
                self.material = Material(image=image)
            if texture:
                self.material = Material(color_texture=texture)

    def __repr__(self):
        return self.name or super().__repr__()

    def __contains__(self, item):
        return (self._positions == item or
                self._normals == item or
                self._texcoords == item or
                self._indices == item or
                self._tangents == item)

    def split_transparency(self, alpha_mode=Material.AlphaMode.BLEND):
        if self.mode and self.mode != self.Mode.TRIANGLES:
            raise NotImplementedError('Prim splitting only implemented for triangles')

        if not self.material or not self.texcoords or (
                self.material.alpha_mode == Material.AlphaMode.OPAQUE):
            raise ValueError('Can\'t split prim: no material or texcoords, or material '
                             'is opaque, or material has no color_texture or diffuse_texture.')

        tex = self.material.color_texture or self.material.diffuse_texture
        if tex is None:
            return
        sampler = tex.sampler or Sampler()
        img = PImage.open(tex.source.get_fp())
        if len(img.getbands()) != 4:
            return
        alpha = img.getdata(3)
        min_alpha, max_alpha = alpha.getextrema()

        # return if all or none of the image is transparent
        if min_alpha == 255 or max_alpha < 255:
            return

        if self.indices:
            indices_iter = (self.indices.data[pos:pos + 3]
                            for pos in
                            range(0, self.indices.count, 3))
        else:
            indices_iter = ((i, i + 1, i + 2)
                            for i in
                            range(0, self.texcoords.count, 3))
        t_indices = []
        o_indices = []
        for indices in indices_iter:
            for point in [self.texcoords.data[i] for i in indices]:
                point = sampler.wrap_point(point)
                x = round((alpha.size[0] - 1) * point[0])
                y = round((alpha.size[1] - 1) * point[1])
                alpha_val = alpha.getpixel((x, y))
                if alpha_val < 255:
                    break
            else:
                o_indices.extend(indices)
                continue
            t_indices.extend(indices)

        # return if there are no opaque vertices
        if not len(o_indices):
            return

        t_material = copy.copy(self.material)
        t_material.alpha_mode = alpha_mode
        # Copy own material in case something else is using it
        self.material = copy.copy(self.material)
        self.material.alpha_mode = Material.AlphaMode.OPAQUE
        self.indices = o_indices

        return Primitive(positions=self.positions, normals=self.normals,
                         texcoords=self.texcoords, tangents=self.tangents,
                         indices=t_indices, material=t_material)

    def render(self, gltf):
        primitive = {'attributes': {}}
        if self.mode:
            primitive['mode'] = self.mode.value
        if self.material:
            primitive['material'] = gltf.index('materials', self.material)
        if self.indices and self.indices.count:
            primitive['indices'] = gltf.index('accessors', self.indices)
        if self.positions and self.positions.count:
            primitive['attributes']['POSITION'] = gltf.index('accessors', self.positions)
        if self.normals and self.normals.count:
            primitive['attributes']['NORMAL'] = gltf.index('accessors', self.normals)
        if self.tangents and self.tangents.count:
            primitive['attributes']['TANGENT'] = gltf.index('accessors', self.tangents)
        if self.texcoords and self.texcoords.count:
            primitive['attributes']['TEXCOORD_0'] = gltf.index('accessors', self.texcoords)
        for i, joints in enumerate(self.joints):
            primitive['attributes']['JOINTS_' + str(i)] = gltf.index('accessors', joints)
        for i, weights in enumerate(self.weights):
            primitive['attributes']['WEIGHTS_' + str(i)] = gltf.index('accessors', weights)
        return primitive

    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self, positions):
        if positions is None:
            self._positions = None
            return
        self._positions = positions if isinstance(positions, Vec3Array) else Vec3Array(positions)

    @property
    def normals(self):
        return self._normals

    @normals.setter
    def normals(self, normals):
        if normals is None:
            self._normals = None
            return
        self._normals = normals if isinstance(normals, Vec3Array) else Vec3Array(normals)

    @property
    def tangents(self):
        return self._tangents

    @tangents.setter
    def tangents(self, tangents):
        if tangents is None:
            self._tangents = None
            return
        self._tangents = tangents if isinstance(tangents, Vec4Array) else Vec4Array(tangents)

    @property
    def texcoords(self):
        return self._texcoords

    @texcoords.setter
    def texcoords(self, texcoords):
        if texcoords is None:
            self._texcoords = None
            return
        self._texcoords = texcoords if isinstance(texcoords, Vec2Array) else Vec2Array(texcoords)

    @property
    def indices(self):
        return self._indices

    @indices.setter
    def indices(self, indices):
        if indices is None:
            self._indices = None
            return
        self._indices = indices if isinstance(indices, ScalarArray) else ScalarArray(indices)


class Mesh(BaseGLTFStructure):
    def __init__(self, mesh=None, gltf=None, name=None):
        self.primitives = []
        if mesh:
            self.name = mesh.get('name')
            for prim in mesh['primitives']:
                self.primitives.append(Primitive(prim, gltf))
        else:
            self.name = name

    def __repr__(self):
        return self.name or super().__repr__()

    def add_primitive(self, **kwargs):
        self.primitives.append(Primitive(**kwargs))
        return len(self.primitives) - 1

    def render(self, gltf):
        mesh = {
            'primitives': [primitive.render(gltf) for primitive in self.primitives]
        }
        if self.name:
            mesh['name'] = self.name

        return mesh


class Camera(BaseGLTFStructure):
    perspective = None
    orthographic = None

    def __init__(self, camera=None, name=None, type=None, perspective=None, orthographic=None):
        if camera:
            self.name = camera.get('name')
            self.type = camera.get('type')
            self.perspective = camera.get('perspective')
            self.orthographic = camera.get('orthographic')
        else:
            self.name = name
            if type is None:
                if perspective is not None:
                    type = 'perspective'
                elif orthographic is not None:
                    type = 'orthographic'
                else:
                    raise ValueError('Camera must have type')
            self.type = type
            self.perspective = perspective
            self.orthographic = orthographic

    def render(self):
        camera = {}
        if self.name is not None:
            camera['name'] = self.name
        if self.type:
            camera['type'] = self.type
        if self.type == 'perspective':
            camera['perspective'] = self.perspective
        elif self.type == 'orthographic':
            camera['orthographic'] = self.orthographic
        return camera


class Node(BaseGLTFStructure):
    mesh = None
    translation = None
    rotation = None
    scale = None
    matrix = None
    skin = None
    camera = None

    def __init__(self, node=None, gltf=None, name=None, mesh=None, children=None,
                 skin=None, camera=None):
        if node:
            self.children = []
            self.name = node.get('name')

            if 'mesh' in node:
                self.mesh = gltf.meshes[node['mesh']]

            if 'camera' in node:
                self.camera = gltf.cameras[node['camera']]

            translation = node.get('translation')
            if translation:
                self.translation = np.array(translation, dtype='float32')

            rotation = node.get('rotation')
            if rotation:
                self.rotation = Quaternion(rotation[3], *rotation[:3])

            scale = node.get('scale')
            if scale:
                self.scale = np.array(scale, dtype='float32')

            matrix = node.get('matrix')
            if matrix:
                self.matrix = np.array(matrix, dtype='float32').reshape((4, 4))

            if matrix and (scale or rotation or translation):
                logger.warning('Node defined both matrix and at least one other transform.')
        else:
            self.name = name
            self.mesh = mesh
            self.children = children or []
            self.skin = skin
            self.camera = camera

    def __repr__(self):
        return self.name or super().__repr__()

    def __eq__(self, other):
        if not (isinstance(other, type(self))
                and (self.mesh, self.name, self.children, self.skin, self.camera) ==
                (other.mesh, other.name, other.children, other.skin, other.camera)):
            return False

        # quaternions seem to blow up if they're compared to None
        if (self.rotation is None) != (other.rotation is None) or self.rotation != other.rotation:
            return False

        return (np.array_equal(self.translation, other.translation) and
                np.array_equal(self.scale, other.scale) and
                np.array_equal(self.matrix, other.matrix))

    def find_children(self, child_indices, gltf):
        for child_idx in child_indices:
            self.children.append(gltf.nodes[child_idx])

    def apply_transforms(self, parent_transformation=None, parent_rotation=None):

        transformation = np.identity(4)
        rotation_matrix = parent_rotation
        if self.scale is not None:
            transformation = transformation.dot(
                np.diag(np.append(self.scale, [1]))
            )
        if self.rotation is not None:
            rotation_matrix = (
                self.rotation.inverse.rotation_matrix.dot(rotation_matrix)
                if rotation_matrix is not None
                else self.rotation.inverse.rotation_matrix
            )
            transformation = transformation.dot(
                self.rotation.inverse.transformation_matrix
            )
        if self.translation is not None:
            translation = np.identity(4)
            translation[3, :] += np.append(self.translation, [0])
            transformation = transformation.dot(translation)

        # Only use self.matrix if there is no other transform
        if self.matrix is not None and np.allclose(transformation, np.identity(4)):
            transformation = self.matrix

        if parent_transformation is not None:
            transformation = transformation.dot(parent_transformation)

            scale = [
                np.linalg.norm(transformation[:3, 0]),
                np.linalg.norm(transformation[:3, 1]),
                np.linalg.norm(transformation[:3, 2]),
            ]

            rotation_matrix = transformation[:3, :3] / scale

        if self.mesh and not np.allclose(transformation, np.identity(4)):
            for p in self.mesh.primitives:
                if not p.positions:
                    continue
                vertices = p.positions.data
                vertices = np.append(vertices, np.ones([len(vertices), 1]), 1)
                p.positions.data = vertices.dot(transformation)[:, :3].astype('float32')
                if p.normals and rotation_matrix is not None:
                    p.normals.data = p.normals.data.dot(rotation_matrix).astype('float32')

        for child in self.children:
            child.apply_transforms(transformation, rotation_matrix)

        self.translation = None
        self.rotation = None
        self.scale = None
        self.matrix = None

    def render(self, gltf):
        node = {}
        if self.mesh:
            node['mesh'] = gltf.index('meshes', self.mesh)
        if self.camera:
            node['camera'] = gltf.index('cameras', self.camera)
        if self.name:
            node['name'] = self.name
        if self.skin:
            node['skin'] = gltf.index('skins', self.skin)
        if self.children:
            node['children'] = [gltf.index_node(n) for n in self.children]
        if self.translation is not None:
            node['translation'] = self.translation.tolist()
        if self.rotation is not None:
            node['rotation'] = self.rotation.elements.tolist()
            node['rotation'].append(node['rotation'].pop(0))
        if self.scale is not None:
            node['scale'] = self.scale.tolist()
        if self.matrix is not None:
            node['matrix'] = self.matrix.reshape((16,)).tolist()
        return node
