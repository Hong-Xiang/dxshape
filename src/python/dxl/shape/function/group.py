from dxl.shape.data import Box, CartesianRepeater
from doufo import List
from doufo.tensor import Vector


# def divide(b: Box, grid: List[int]) -> List[Box]:
#     subbox_prototype = Box(sub_box_shape(b, grid), b.origin)
#     return (moves(offsets(sub_box_shape(b, grid), b.origin, grid))
#             .fmap(lambda v: subbox_prototype.translate(v)))

def offsets(step, grid: List[int]):
    steps = [[s*i for i in range(g)]
             for s, g in zip(step, grid)]
    return steps

def sub_box_shape(b: Box, grid: List[int]) -> Vector:
    return Vector([s / g for s, g in zip(b.shape, grid)])

# def offsets(step, origin, grid: List[int]) -> Vector:
#     steps = [[s*i - o/2 for i in range(g)]
#              for s, g, o in zip(step, grid, origin)]
#     return steps
def moves(steps):
    xs, ys, zs = steps
    return List([Vector([x, y, z]) for x in xs for y in ys for z in zs])


