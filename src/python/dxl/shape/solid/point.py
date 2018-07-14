from .base import Solid, Shape
from ..utils.axes import AxisBase
from ..utils.vector import VectorLowDim 
from ..rotation.matrix import rotate3
import numpy as np

__all__ = ["Point"]


class Point(Shape):
    def __init__(self, data: VectorLowDim):
        if isinstance(data, (list, tuple)):
            data = VectorLowDim.from_list(data)
        self._data = data

    def dim(self):
        return self._data.dim()

    def origin(self):
        return self._data

    def translate(self, v: VectorLowDim) -> 'Point':
        return Point(self.origin() + v)

    def rotate_origin(self, axis: AxisBase, angle: float) -> 'Solid':
        RotateMatrix=rotate3(theta=angle, axis=axis)
        pRot=np.dot(RotateMatrix, self)
        return pRot

    def is_in(self, s: Solid) -> bool:
        return s.is_collision(self)
