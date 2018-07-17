from ..utils import VectorLowDim, AngleBase, AxisBase

from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

class LinearSpace(Shape):
    @property
    def ndim(self):
        pass

class Entity(metaclass=ABCMeta):
    
    @property
    def origin(self):
        return self._origin
    
    @property
    def normal(self):
        return self._normal

    def __init__(self, origin, normal, *, space=None):
        self._origin = np.array(origin)
        # TODO: add unit vector check
        self._normal = np.array(normal)
        if len(self.origin) != len(self.normal):
            raise ValueError(f"origin {self.origin} and normal {self.normal} dimension is not equal")
        self._space = space

    def ndim(self):
        return len(self.origin)

    def translate(self, v):
        return self.replace(origin=self.origin + v)

    @abstractmethod
    def _rotate_on_direction(self, direction, theta):
        pass

    def rotate(self, axis, theta: float):
        if np.allclose(axis.origin, 0.0):
            return self._rotate_on_direction(axis.direction, theta)
        return (self.translate(-axis.origin)
                .rotate(axis.translate(-axis.origin).direction, theta)
                .translate(axis.origin))

    def _replace_dict(self, origin, normal):
        return {
            'origin': origin if origin is not None else self.origin,
            'normal': normal if normal is not None else self.normal
        }

    def replace(self, *, origin=None, normal=None):
        return Entity(**self._replace_dict(origin, normal))

    def is_collision(self, s: 'Entity') -> bool:
        pass




class R3(LinearSpace):
    @property
    def ndim(self):
        return 3


