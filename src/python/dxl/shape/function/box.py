from dxl.shape.data import Box
from dxl.data import List
from dxl.shape.data import Vector


def divide(b: Box, grid: List[int]) -> List[Box]:
    subbox_prototype == Box(sub_box_shape(b, grid))


def sub_box_shape(b: Box, grid: List[int]) -> Vector:
    return Vector([s / g for s, g in zip(b.shape, grid)])


def offsets(b: Box, grid: List[int]) -> Vector:
    step = sub_box_shape(b, grid)
    steps = [[s*i - o/2 for i in range(g)]
             for s, g, o in zip(step, grid, b.origin)]
    return steps
