from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

from dxl.data import DataClass
from doufo.tensor import Vector, Matrix, all_close
from dxl.data import Functor
from dxl.function import replace


__all__ = ['Existence', 'Entity']


class Existence(DataClass):
    @abstractproperty
    def ndim(self):
        pass


class Entity(Existence, Functor):
    @property
    def ndim(self):
        return len(self.origin)

    def translate(self, v: Vector):
        return replace(self, origin=self.origin + v)

    def fmap(self, f):
        pass

    # @abstractmethod
    # def rotate_on_direction(self, direction, theta):
    #     pass

    def rotate(self, axis: 'Axis', theta):
        from dxl.shape.function import rotate
        return (self.translate(-axis.origin)
                .fmap(lambda v: rotate(v, axis.normal, theta))
                # .rotate_on_direction(axis.direction_vector, theta)
                .translate(axis.origin))
