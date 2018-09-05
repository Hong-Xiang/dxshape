from dxl.shape.function.group import offsets, sub_box_shape, Box, Vector, List
from doufo.tensor import all_close


def test_sub_box_shape():
    assert all_close(sub_box_shape(Box([1.0, 2.0, 3.0]), [10, 40, 30]),
                     Vector([0.1, 0.05, 0.1]))


def test_offsets():
    assert (offsets([0.5, 0.5, 0.5], [2, 4, 6])
            == [[0.0, 0.5], [0.0, 0.5, 1.0, 1.5], [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]])
