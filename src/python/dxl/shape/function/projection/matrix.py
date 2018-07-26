from dxl.shape.data import Vector, Matrix
from .function import proj, embed
from dxl.function.tensor import transpose
from dxl.data import List

__all__ = ['proj3to2', 'embed2to3']


def proj3to2(n: Vector) -> Matrix:
    es = List([Vector([1.0, 0.0, 0.0]),
               Vector([0.0, 1.0, 0.0]),
               Vector([0.0, 0.0, 1.0])])
    vs = es.fmap(lambda v: proj(v, n))
    return transpose(Matrix([vs[0].join(), vs[1].join(), vs[2].join()]))


def embed2to3(n: Vector) -> Matrix:
    es = List([Vector([1.0, 0.0]),
               Vector([0.0, 1.0])])
    vs = es.fmap(lambda v: embed(v, n)).fmap(lambda v: v.join())
    return transpose(Matrix(vs))
