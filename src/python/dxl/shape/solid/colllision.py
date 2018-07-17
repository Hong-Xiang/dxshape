from .base import Shape
from .point import Point
from .box import Box
from ..rotation.matrix import axis_to_axis
from ..utils.vector import Vector3
import numpy as np


class CollisionTesterManager:
    @classmethod
    def get(s0: Shape, s1: Shape):
        pass


#class CollisionTester:
#    def is_collision( s0: Shape, s1: Shape) -> bool:
#       pass


#class BoxPointTester:
#    def __init__(self, p: Point, b: Box):
#        if isinstance(p, Box):
#            p, b = b, p
#        self._point = p
#        self._box = b

