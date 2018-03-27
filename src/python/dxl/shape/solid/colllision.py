from .base import Shape, Point
from .box import Box
import numpy as np


class CollisionTesterManager:
    @classmethod
    def get(s0: Shape, s1: Shape):
        pass


class CollisionTester:
    def is_collision(s0: Shape, s1: Shape) -> bool:
        pass


class BoxPointTester:
    def is_collision(p: Point, b: Box) -> bool:
        if isinstance(p, Box):
            p, b = b, p
        p = np
