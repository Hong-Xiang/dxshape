from .base import Entity, Vector
from dxl.function.tensor.compare import all_close
import numpy as np
import math


class Box(Entity):
    __slots__ = ['shape', 'origin', 'normal']

    def __init__(self,
                 shape: Vector,
                 origin: Vector = None,
                 normal: Vector = None):
        self.shape = Vector(shape)
        if origin is None:
            origin = Vector([0.0, 0.0, 0.0])
        self.origin = Vector(origin)
        if normal is None:
            normal = Vector([0.0, 0.0, 1.0])
        self.normal = Vector(normal)

    # def rotate_on_direction(self, direction, theta):
    #     from .point import Point
    #     p_origin = Point(self.origin)
    #     p_normal = Point(self.normal)
    #     return self.replace(origin=p_origin._rotate_on_direction(direction, theta).origin,
    #                         normal=p_normal._rotate_on_direction(direction, theta).origin)

    def is_collision(self, p: 'Entity') -> bool:
        from dxl.shape.data.axis import Axis
        from dxl.shape.function.rotation.matrix import axis_to_z 
        p_tran_rot = axis_to_z(self.normal) @ p.translate(-self.origin).origin
        for i in range(3):
            if any(abs(p_tran_rot) > self.shape[i] / 2):
                return False
        return True

    def fmap(self, f):
        return Box(self.shape, f(self.origin), f(self.normal))

    def __eq__(self, b):
        if not isinstance(b, Box):
            return False
        return all_close(self.shape, b.shape) and all_close(self.origin, b.origin) and all_close(self.normal, b.normal)
