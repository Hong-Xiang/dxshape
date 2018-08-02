import numpy as np

from dxl.shape.data import Point, Box


class CollisionCheckers:
    collision_checkers = {}

    @classmethod
    def find_checker(cls, s0, s1):
        return cls.collision_checkers.get(type(s0), {}).get(type(s1))

    @classmethod
    def register(cls, s0, s1, func):
        if cls.collision_checkers.get(s0) is None:
            cls.collision_checkers[s0] = {}
        cls.collision_checkers[s0][s1] = func


def is_collision(s0, s1):
    checker = CollisionCheckers.find_checker(s0, s1)
    if checker is not None:
        return checker(s0, s1)
    checker = CollisionCheckers.find_checker(s0, s1)
    if checker is not None:
        return checker(s1, s0)
    raise NotImplementedError("No checker for ({}, {}) is implemented.".format(
        type(s0), type(s1)))


def point_box_checker(p, b):
    return b.is_collision(p)


CollisionCheckers.register(Point, Box, point_box_checker)