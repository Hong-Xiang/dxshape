from dxl.shape.data import Box, CartesianRepeater, RingRepeater
from dxl.data import List
from dxl.shape.data import Vector


# def divide(b: Box, grid: List[int]) -> List[Box]:
#     subbox_prototype = Box(sub_box_shape(b, grid), origin=b.origin)
#     return CartesianRepeated(subbox_prototype, subbox_prototype.shape, grid).flatten()
    # return (moves(offsets(sub_box_shape(b, grid), b.origin, grid))
    # .fmap(lambda v: subbox_prototype.translate(v)))

def divide(b: Box, grid: List[int]):
    subbox_prototype = Box(sub_box_shape(b, grid), b.origin)
    return CartesianRepeater(subbox_prototype, subbox_prototype.shape, grid).flatten()

def linear_divide(b:Box, step, grid: List[int]):
    subbox_prototype = Box(sub_box_shape(b, grid), b.origin)
    #return CRepeater(subbox_prototype, step, grid).flatten()
    return CartesianRepeater(subbox_prototype, step, grid).flatten()

def ring_divide(b:Box, step, num, axis):
    return RingRepeater(b, step, num, axis).flatten()

def sub_box_shape(b: Box, grid: List[int]) -> Vector:
    return Vector([s / g for s, g in zip(b.shape, grid)])
