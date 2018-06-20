from .base import Solid
from ..utils.vector import VectorLowDim, Vector3
from ..utils.angle import AngleBase, SolidAngle
from .line import Line


class Box(Solid):
    def __init__(self,
                 shape: Vector3,
                 origin: Vector3 = None,
                 normal: SolidAngle = None):
        self._shape = Vector3(shape)
        if origin is None:
            origin = Vector3([0.0, 0.0, 0.0])
        self._origin = Vector3(origin)
        if normal is None:
            normal = SolidAngle(0.0, 0.0)
        self._normal = Vector3(normal)

    @property
    def dim(self):
        return 3

    def shape(self):
        return self._shape

    def normal(self):
        return self._normal.to_direction_vector()

    def origin(self):
        return self._origin

    def rotate_origin(self, angle: SolidAngle) -> 'Box':
        pass

    def rotate(self, axis, theta):
        pass

    def translate(self, v: VectorLowDim) -> 'Box':
        return Box(
            shape=self.shape(),
            origin=self.translate_origin(v),
            normal=self.normal())

    def edges(self) -> 'List[Line]':
        pass
