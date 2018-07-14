from ..utils import VectorLowDim, AngleBase, AxisBase

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def dim(self):
        pass

    @abstractmethod
    def origin(self) -> VectorLowDim:
        pass

    def translate_origin(self, v: VectorLowDim):
        return self.origin - v

    @abstractmethod
    def translate(self, v: VectorLowDim) -> 'Shape':
        pass

    @abstractmethod
    def rotate_origin(self, axis: AxisBase, angle: float) -> 'Solid':
        pass


class LinearSpace(Shape):
    @property
    def ndim(self):
        pass

    @property
    def true_dim(self):
        pass

class R3(LinearSpace):
    pass


class Solid(Shape):
    @abstractmethod
    def normal(self) -> VectorLowDim:
        pass

    def is_collision(self, s: Shape) -> bool:
        pass
