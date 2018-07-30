import numpy as np

from dxl.shape.data import AXIS3_Z, Axis
from .axis import Axis
from .base import Entity, Vector

__all__ = ["Point"]


class Point(Entity):
    __slots__ = ['origin']

    def __init__(self, origin):
        self.origin = Vector(origin)

    def fmap(self, f):
        return Point(f(self.origin))

    def is_in(self, s: 'Entity') -> bool:
        return s.is_collision(self)
