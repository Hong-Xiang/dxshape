from doufo.tensor import Vector, Matrix
from .function import proj, embed
from doufo.tensor import transpose
from doufo import List

__all__ = ['proj3to2', 'embed2to3']


def proj3to2(n: Vector) -> Matrix:
    es = List([Vector([1.0, 0.0, 0.0]),
               Vector([0.0, 1.0, 0.0]),
               Vector([0.0, 0.0, 1.0])])
    vs = es.fmap(lambda v: proj(v, n))
    return transpose(Matrix([vs[0].unbox(), vs[1].unbox(), vs[2].unbox()]))


def embed2to3(n: Vector) -> Matrix:
    es = List([Vector([1.0, 0.0]),
               Vector([0.0, 1.0])])
    vs = es.fmap(lambda v: embed(v, n)).fmap(lambda v: v.unbox())
    return transpose(Matrix(vs))
