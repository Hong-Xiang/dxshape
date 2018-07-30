from dxl.shape.data import Box, CartesianRepeated
from dxl.data import List
from dxl.shape.data import Vector


def divide(b: Box, grid: List[int]) -> List[Box]:
    subbox_prototype = Box(sub_box_shape(b, grid), origin=b.origin)
    return CartesianRepeated(subbox_prototype, subbox_prototype.shape, grid).flatten()
    # return (moves(offsets(sub_box_shape(b, grid), b.origin, grid))
    # .fmap(lambda v: subbox_prototype.translate(v)))


def sub_box_shape(b: Box, grid: List[int]) -> Vector:
    return Vector([s / g for s, g in zip(b.shape, grid)])
