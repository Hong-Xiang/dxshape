from .base import Solid, Shape
from ..utils.vector import VectorLowDim

__all__ = ['Point', 'Origin']


class Point(Shape):
    def __init__(self, data: VectorLowDim):
        if isinstance(data, (list, tuple)):
            data = VectorLowDim.from_list(data)
        self._data = data

    def data(self):
        return self._data

    def dim(self):
        return self._data.dim()

    def origin(self):
        return self._data

    def rotate_origin(self, theta):
        raise NotImplementedError

    def translate(self, v: VectorLowDim) -> 'Point':
        return Point(self.origin() + v)

    def translate_origin(self, v) -> 'Point':
        raise NotImplementedError

    def rotate(self, axis, theta) -> 'Point':
        pass

    def is_in(self, s: Solid) -> bool:
        from dxl.shape.binary_ops import is_collision
        return is_collision(self, s)

    def __sub__(self, v):
        return Point(self._data - v)

    def __mul__(self, v):
        return Point(self.data() * v.data())

    def __getitem__(self, i):
        return self._data[i]


class Origin(Point):
    def __init__(self, ndim=None):
        from ..utils import get_default_space
        if ndim is None:
            ndim = get_default_space().ndim
        super().__init__(VectorLowDim([0.0] * ndim))
