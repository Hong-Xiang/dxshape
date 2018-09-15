from dxl.shape.data import Box, CartesianRepeater, RingRepeater
from doufo import List
from doufo.tensor import Vector


# def divide(b: Box, grid: List[int]) -> List[Box]:
#     subbox_prototype = Box(sub_box_shape(b, grid), origin=b.origin)
#     return CartesianRepeated(subbox_prototype, subbox_prototype.shape, grid).flatten()
# return (moves(offsets(sub_box_shape(b, grid), b.origin, grid))
# .fmap(lambda v: subbox_prototype.translate(v)))

def divide(b: Box, grid: List[int]):
    subbox_prototype = Box(sub_box_shape(b, grid), b.origin)
    return CartesianRepeater(subbox_prototype, subbox_prototype.shape, grid).flatten()


def linear_divide(b: Box, step, grid: List[int]):
    subbox_prototype = Box(sub_box_shape(b, grid), b.origin)
    # return CRepeater(subbox_prototype, step, grid).flatten()
    return CartesianRepeater(subbox_prototype, step, grid).flatten()


def ring_divide(b: Box, step, num, axis):
    return RingRepeater(b, step, num, axis).flatten()


def sub_box_shape(b: Box, grid: List[int]) -> Vector:
    return Vector([s / g for s, g in zip(b.shape, grid)])


def norm0(v, eps=1e-5):
    result = 0
    for x in v:
        if abs(x) > eps:
            result += 1
    return result


def vertices(b: Box):
    from dxl.shape.data import Point
    from itertools import product
    from dxl.shape.function.api import rotate_by_matrix
    from dxl.shape.function.rotation.matrix import axis_to_axis
    ps = []
    for signs in product(*[(-1, 1)]*3):
        ps.append([sign*size/2 for sign, size in zip(signs, b.shape)])
    ps = [Point(p) for p in ps]
    m = axis_to_axis([0.0, 0.0, 1.0], b.normal)
    ps = [rotate_by_matrix(p, m) for p in ps]
    ps = [p.translate(b.origin) for p in ps]
    return ps

def edges(b: Box):
    from dxl.shape.data import Segment
    es = adjs()
    ps = vertices(b)
    return [Segment(ps[i], ps[j]) for i, j in es]

from functools import lru_cache

@lru_cache(1)
def adjs():
    ps = vertices(Box([1.0, 2.0, 3.0]))
    result = []
    for i, p in enumerate(ps):
        for j, q in enumerate(ps):
            if i <= j:
                continue
            if norm0(p.origin - q.origin) == 1:
                result.append((i, j))
    return result
