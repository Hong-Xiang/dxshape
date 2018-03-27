from .vector import Vector3, VectorLowDim
from abc import ABCMeta, abstractmethod
import numpy as np


class AxisBase(metaclass=ABCMeta):
    @abstractmethod
    def direction_vector(self) -> VectorLowDim:
        pass


class Axis3(AxisBase):
    def __init__(self, direction_vector: Vector3):
        if isinstance(direction_vector, np.ndarray):
            direction_vector = Vector3(direction_vector)
        self._v = direction_vector

    def direction_vector(self) -> Vector3:
        return self._v


AXIS3_X = Axis3(Vector3([1.0, 0.0, 0.0]))
AXIS3_Y = Axis3(Vector3([0.0, 1.0, 0.0]))
AXIS3_Z = Axis3(Vector3([0.0, 0.0, 1.0]))


class Axes3:
    def __init__(self, x_axis, y_axis, z_axis):
        self._x = x_axis
        self._y = y_axis
        self._z = z_axis

    def x(self) -> Axis3:
        return self._x

    def y(self) -> Axis3:
        return self._y

    def z(self) -> Axis3:
        return self._z


AXES3_STD = Axes3(AXIS3_X, AXIS3_Y, AXIS3_Z)
