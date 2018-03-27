from .base import Solid
from ..vector import VectorLowDim, Vector3
from ..angle import AngleBase, SolidAngle


class Box(Solid):
    def __init__(self, shape: Vector3, origin: Vector3=None, normal: SolidAngle=None):
        self._shape = Vector3(shape)
        if origin is None:
            origin = Vector3([0.0, 0.0, 0.0])
        self._origin = Vector3(origin)
        if normal is None:
            normal = SolidAngle(0.0, 0.0)
        self._normal = Vector3(normal)

    def shape(self):
        return self._shape

    def normal(self):
        return self._normal.direction_vector()

    def origin(self):
        return self._origin

    def rotate_origin(self, angle: SolidAngle) -> 'Box':
        pass

    def translate(self, v: VectorLowDim) -> 'Box':
        return Box(shape=self.shape(),
                   origin=self.translate_origin(v),
                   normal=self.normal())
