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
        return self.origin + v

    @abstractmethod
    def tanslate(self, v: VectorLowDim) -> 'Shape':
        pass

    @abstractmethod
    def rotate_origin(self, axis: AxisBase, angle: float) -> 'Solid':
        pass


class Solid(Shape):
    @abstractmethod
    def normal(self) -> VectorLowDim:
        pass

    def is_collision(self, s: 'Shape') -> bool:
        pass
