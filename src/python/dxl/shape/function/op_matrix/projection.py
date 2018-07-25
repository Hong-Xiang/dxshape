from dxl.function.tensor import transpose
from dxl.shape.function import project, embed
from dxl.shape.data import Vector, Matrix
from dxl.data import List


def project3to2(n: Vector):
    es = List([Vector([1.0, 0.0, 0.0]),
               Vector([0.0, 1.0, 0.0]),
               Vector([0.0, 0.0, 1.0])])
    vs = es.fmap(lambda v: project(v, n))
    return transpose(Matrix([vs[0].join(), vs[1].join()]))


def embed2to3(n: Vector):
    es = List([Vector([1.0, 0.0]),
               Vector([0.0, 1.0])])
    vs = es.fmap(lambda v: embed(v, n)).fmap(lambda v: v.join())
    return transpose(Matrix(vs))
