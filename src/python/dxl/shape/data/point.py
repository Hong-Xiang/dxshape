import numpy as np

from dxl.shape.data import AXIS3_Z, Axis, Entity
from doufo.tensor import Vector

__all__ = ["Point"]

@dataclass
class Point(Entity):
    origin: Vector

    def fmap(self, f):
        return Point(f(self.origin))

    def is_in(self, s: 'Entity') -> bool:
        return s.is_collision(self)

    @property
    def x(self):
        return self.origin.x

    @property
    def y(self):
        return self.origin.y

    @property
    def z(self):
        return self.origin.z

    def __getitem__(self, s):
        return self.origin[s]