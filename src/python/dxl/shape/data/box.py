from .base import Entity, Vector
import numpy as np
import math


class Box(Entity):
    __slot__ = ['shape', 'origin', 'normal']

    def __init__(self,
                 shape: np.ndarray,
                 origin: np.ndarray = None,
                 normal: np.ndarray = None):
        if isinstance(shape, (list, tuple)):
            shape = np.asarray(shape)
        self.shape = shape
        if origin is None:
            origin = np.array([0.0, 0.0, 0.0])
        if isinstance(origin, (list, tuple)):
            origin = np.asarray(origin)
        self.origin = origin
        if normal is None:
            normal = np.array([0.0, 0.0, 1.0])
        if isinstance(normal, (list, tuple)):
            normal = np.asarray(normal)
        self.normal = normal

    def rotate_on_direction(self, direction, theta):
        from .point import Point
        p_origin = Point(self.origin)
        p_normal = Point(self.normal)
        return self.replace(origin=p_origin._rotate_on_direction(direction, theta).origin,
                            normal=p_normal._rotate_on_direction(direction, theta).origin)

    def is_collision(self, p: 'Entity') -> bool:
        from .axis import Axis
        from dxl.shape.function.rotation import axis_to_z
        p_tran = p.translate(self.origin)
        rot_matrix = axis_to_z(self.normal)
        p_tran_rot = np.dot(rot_matrix, p_tran.origin)
        for i in range(3):
            if any(abs(p_tran_rot) > self.shape[i] / 2):
                return False
        return True

    def fmap(self, f):
        return Box(self.shape, f(self.origin), f(self.normal))

    def __eq__(self, b):
        if not isinstance(b, Box):
            return False
        return np.allclose(self.shape, b.shape) and np.allclose(self.origin, b.origin) and np.allclose(self.normal, b.normal)
