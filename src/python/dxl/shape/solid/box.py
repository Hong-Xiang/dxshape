from .base import Solid
from .point import Point
from ..utils.vector import VectorLowDim, Vector3
from ..utils.angle import AngleBase, SolidAngle
from ..rotation.matrix import axis_to_axis
from ..utils.axes import Axes, Axis3, AXIS3_Z
import numpy as np
import math

class Box(Solid):
    def __init__(self, shape: Vector3, origin: Vector3=None, normal: SolidAngle=None):
        self._shape = Vector3(shape)
        if origin is None:
            origin = Vector3([0.0, 0.0, 0.0])
        self._origin = Vector3(origin)
        if normal is None:
            normal = SolidAngle(0.0, 0.0)
        self._normal = normal

    def dim(self):
        pass

    def shape(self):
        return self._shape

    def normal(self):
        return self._normal

    def origin(self):
        return self._origin

    def rotate_origin(self, axis: Axes=None, angle: float=None, rotate_matrix: np.array=None) -> 'Box':
        point_origin = Point(self.origin())
        point_normal = Point(self._normal.direction_vector())
        rotate_origin = point_origin.rotate_origin(axis, angle, rotate_matrix)
        rotate_normal = point_normal.rotate_origin(axis, angle, rotate_matrix).origin()
        solid_normal = SolidAngle.from_direction_vector(rotate_normal)
        return Box(shape=self.shape(),
                   origin=rotate_origin.origin(),
                   normal=solid_normal)

    def translate(self, v: VectorLowDim) -> 'Box':
        return Box(shape=self.shape(),
                   origin=self.translate_origin(v),
                   normal=self.normal())
    
