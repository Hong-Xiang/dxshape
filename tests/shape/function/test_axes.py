from dxl.shape.function.axes import axis_x_of, axis_y_of
from dxl.shape.data import Vector
import math
import pytest
from dxl.function.tensor import all_close


@pytest.mark.parametrize('v, expect', [
    ([0.0, 0.5, 0.5], Vector([0.0, math.sqrt(2) / 2.0, -math.sqrt(2) / 2.0])),
    ([0.0, 1.0, 0.0], Vector([0.0, 1.0, 0.0])),
    ([0.0, 0.0, 1.0], Vector([0.0, 0.0, 1.0])),
])
def test_axis_x_of(v, expect):
    assert all_close(axis_x_of(v), expect)
