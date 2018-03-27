from .base import Solid, Shape
from ..utils.vector import VectorLowDim

__all__ = [Point]


class Point(Shape):
    def __init__(self, data: VectorLowDim):
        if isinstance(data, (list, tuple)):
            data = VectorLowDim.from_list(data)
        self._data = data

    def dim(self):
        return self._data.dim()

    def origin(self):
        return self._data

    def tanslate(self, v: VectorLowDim) -> 'Point':
        return Point(self.origin() + v)

    def is_in(self, s: Solid) -> bool:
        return s.is_collision(self)
