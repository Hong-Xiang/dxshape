from dxl.shape.data import Vector, Matrix
from dxl.function.tensor import all_close, argmax, project
from dxl.data import List

# TODO enhance logic since lots of duplication

__all__ = ['proj', 'embed']


def proj(v: Vector, n: Vector):
    v, n = Vector(v), Vector(n)
    p = project(v, n)
    return Vector([p[i] for i in range(v.size) if i != argmax(n)])


def embed(v: Vector, n: Vector):
    v, n = Vector(v), Vector(n)
    from ..axes import axis_x_of, axis_y_of
    return Vector([axis_x_of(n) * v.x, axis_y_of(n) * v.y])
