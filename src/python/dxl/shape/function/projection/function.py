from doufo.tensor import Vector, Matrix
from doufo.tensor import all_close, argmax, project
from doufo import List

# TODO enhance logic since lots of duplication

__all__ = ['proj', 'embed']

from numba import jit
import numpy as np


def proj(v: Vector, n: Vector):
    v, n = Vector(v), Vector(n)
    p = project(v, n)
    return Vector([p[(np.argmax(n) + i + 1) % len(p)] for i in range(v.size - 1)])
    # return Vec[p[(np.argmax(n) + i + 1) % len(p)] for i in range(v.size - 1)]
    # return Vector(np.array([1, 1]))


def embed(v: Vector, n: Vector):
    v, n = Vector(v), Vector(n)
    from ..axes import axis_x_of, axis_y_of
    return axis_x_of(n) * v.x + axis_y_of(n) * v.y
