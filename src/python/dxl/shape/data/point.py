import numpy as np

from dxl.shape.data import AXIS3_Z, Axis
from dxl.shape.function.rotation.matrix import (
    axis_to_z, rotate2, rotate3, z_to_axis)
from .axis import Axis
from .base import Entity, Vector

__all__ = ["Point"]


class Point(Entity):
    __slots__ = ['origin']

    def __init__(self, origin):
        self.origin = Vector(origin)

    def rotate_on_direction(self, direction: Vector, theta: float):
        from dxl.shape.rotation.matrix import rotate2, rotate3, axis_to_z, z_to_axis
        if self.ndim == 2:
            return self.replace(origin=rotate2(theta)@self.origin)
        elif self.ndim == 3:
            origin = (axis_to_z(Axis(direction)) @ rotate3(theta, AXIS3_Z)
                      @ z_to_axis(Axis(direction)) @ self.origin)
            return self.replace(origin=origin)
    
    def fmap(self, f):
        return Point(f(self.origin))

    def is_in(self, s: 'Entity') -> bool:
        return s.is_collision(self)
