from dxl.shape.function import proj
from dxl.shape.data import Vector
from dxl.function.tensor import all_close
import pytest

@pytest.mark.parametrize('v,n,expect', [
    ([1.0, 1.0, 0.0], [1.0, 0.0, 0.0], Vector([1.0, 0.0])),
    ([1.0, 2.0, 3.0], [1.0, 0.0, 0.0], Vector([2.0, 3.0]))
])
def test_proj(v, n, expect):
    assert all_close(proj(v, n), expect)
