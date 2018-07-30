from .base import Entity
import numpy as np

from dxl.data.tensor import Vector

__all__ = ['Axis', 'AXIS3_X', 'AXIS3_Y', 'AXIS3_Z', 'AXES3']


class Axis(Entity):
    __slots__ = ('normal', 'origin')

    def __init__(self, normal: Vector, origin: Vector = None):
        if isinstance(normal, Axis):
            normal, origin = Vector(normal.normal), Vector(normal.origin)
        self.normal = Vector(normal)
        if origin is None:
            origin = Vector([0.0, 0.0, 0.0])
        self.origin = Vector(origin)

    def rotate_on_direction(self, direction: Vector, theta: float):
        from dxl.shape.function import rotate
        return self.replace(normal = rotate(self.normal, direction, theta),
                            origin = rotate(self.origin, direction, theta))

    def fmap(self, f):
        return Axis(f(self.normal), f(self.origin))


AXIS3_X = Axis([1.0, 0.0, 0.0])
AXIS3_Y = Axis([0.0, 1.0, 0.0])
AXIS3_Z = Axis([0.0, 0.0, 1.0])


class AXES3:
    x = AXIS3_X
    y = AXIS3_Y
    z = AXIS3_Z
