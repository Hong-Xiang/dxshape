from .base import Solid, Shape

__all__ = [Point]


class Point(Shape):
    def __init__(self, data: VectorLowDim):
        self._data = data

    def dim(self):
        return self._data.dim()

    def origin(self):
        return self._data

    def tanslate(self):
        return Point()

    def is_in(self, s: Solid) -> bool:
        return s.is_collision(self)
