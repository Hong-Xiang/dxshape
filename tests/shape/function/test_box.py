from dxl.shape.function.box import Box, Vector, List, divide, sub_box_shape
from dxl.shape.data import Group
from dxl.function.tensor import all_close


def test_sub_box_shape():
    assert all_close(sub_box_shape(Box([1.0, 2.0, 3.0]), [10, 40, 30]),
                     Vector([0.1, 0.05, 0.1]))

def test_divide():
    result = divide(Box([1.0, 2.0, 3.0]), [10, 20, 30])
    assert len(result) == 10 * 20 * 30

