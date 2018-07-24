from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

from dxl.data import DataClass
from dxl.function import replace


class LinearSpace:
    @property
    def ndim(self):
        pass


class Entity(DataClass):
    @property
    def ndim(self):
        return len(self.origin)

    def translate(self, v: np.ndarray):
        return replace(self, origin=np.array(self.origin) + v)

    @abstractmethod
    def _rotate_on_direction(self, direction, theta):
        pass

    def rotate(self, axis: 'Axis', theta: float):
        from dxl.shape.solid.axis import Axis
        if np.allclose(axis.origin, 0.0):
            return self._rotate_on_direction(axis.direction_vector, theta)
        return (self.translate(-axis.origin)
                ._rotate_on_direction(axis.direction_vector, theta)
                .translate(axis.origin))


class R3(LinearSpace):
    @property
    def ndim(self):
        return 3
