from .base import Entity
from .point import Point
import numpy as np
#from abc import ABCMeta


class Axis(Entity):
    __slot__ = ['direction_vector', 'origin']
    def __init__(self, direction_vector: np.ndarray, origin: np.ndarray = None):
        if isinstance(direction_vector, (list,tuple)):
            direction_vector = np.asarray(direction_vector)
        self.direction_vector = direction_vector
        if origin is None:
            origin = np.array([0.0, 0.0, 0.0])
        self.origin = origin
   
    def _rotate_on_direction(self, direction: np.ndarray, theta: float):
        p_origin = Point(self.origin)
        p_direction = Point(self.direction_vector)
        return self.replace(direction_vector = p_direction._rotate_on_direction(direction, theta).origin,
                            origin = p_origin._rotate_on_direction(direction, theta).origin)

AXIS3_X = Axis(np.array([1.0, 0.0, 0.0]))
AXIS3_Y = Axis(np.array([0.0, 1.0, 0.0]))
AXIS3_Z = Axis(np.array([0.0, 0.0, 1.0]))

# class Axes3:
#     """
#     A coordinate framework with three axis
#     """

#     def __init__(self, x_axis, y_axis, z_axis):
#         self._x = x_axis
#         self._y = y_axis
#         self._z = z_axis

#     def x(self) -> Axis:
#         return self._x

#     def y(self) -> Axis:
#         return self._y

#     def z(self) -> Axis:
#         return self._z


# AXES3_STD = Axes3(AXIS3_X, AXIS3_Y, AXIS3_Z)