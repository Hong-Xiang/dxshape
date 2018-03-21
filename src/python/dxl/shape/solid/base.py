from ..vector import VectorLowDim
from ..angle import AngleBase
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


class Solid(Shape):
    @abstractmethod
    def normal(self) -> VectorLowDim:
        pass

    @abstractmethod
    def rotate(self, axis: VectorLowDim, radian: float) -> 'Solid':
        pass

    def is_collision(self, s: 'Shape') -> bool:
        pass
