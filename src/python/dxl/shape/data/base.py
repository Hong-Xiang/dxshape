from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

from dxl.data import DataClass
from dxl.data.tensor import Vector, Matrix
from dxl.function import replace
from dxl.function.tensor import all_close

__all__ = ['Existence', 'Entity']


class Existence(DataClass):
    @abstractproperty
    def ndim(self):
        pass


class Entity(Existence):
    @property
    def ndim(self):
        return len(self.origin)

    def translate(self, v: Vector):
        return replace(self, origin=np.array(self.origin) + v)

    @abstractmethod
    def rotate_on_direction(self, direction, theta):
        pass

    def rotate(self, axis: 'Axis', theta):
        if all_close(axis.origin, 0.0):
            return self.rotate_on_direction(axis.direction_vector, theta)
        return (self.translate(-axis.origin)
                .rotate_on_direction(axis.direction_vector, theta)
                .translate(axis.origin))
