from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

from doufo import DataClass, Functor, replace
from doufo.tensor import Vector, Matrix, all_close

__all__ = ['Existence', 'Entity']


class Existence(DataClass):
    @abstractproperty
    def ndim(self):
        pass


class Entity(Existence, Functor):
    origin: Vector
    @property
    def ndim(self):
        return len(self.origin)

    def translate(self, v: Vector):
        return replace(self, origin=self.origin + v)

    def fmap(self, f):
        pass

    def unbox(self):
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
