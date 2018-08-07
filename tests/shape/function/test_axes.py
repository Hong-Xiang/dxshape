from dxl.shape.function.axes import axis_x_of, axis_y_of, abs_
from dxl.shape.data import Vector
import math
import pytest
from doufo.tensor import all_close


@pytest.mark.parametrize('v, expect', [
    ([0.0, 0.0, 1.0], Vector([1.0, 0.0, 0.0])),
    ([0.0, 0.5, 0.5], Vector([0.0, -math.sqrt(2) / 2.0, math.sqrt(2) / 2.0])),
    ([0.0, 0.0, 1.0], Vector([1.0, 0.0, 0.0])),
])
def test_axis_x_of(v, expect):
    assert all_close(axis_x_of(v), expect)


@pytest.mark.parametrize('v, expect', [
    ([0.0, 0.0, 1.0], Vector([0.0, 1.0, 0.0])),
])
def test_axis_y_of(v, expect):
    assert all_close(axis_y_of(v), expect)


def test_axis_x_and_axis_y_consistance():
    n = Vector([1.0, 2.0, 3.0])
    assert abs(axis_x_of(n) @ axis_y_of(n)) < 1e-6
    assert abs(axis_x_of(n) @ n) < 1e-6
    assert abs(axis_y_of(n) @ n) < 1e-6
