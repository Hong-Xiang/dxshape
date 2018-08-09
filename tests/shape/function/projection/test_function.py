from dxl.shape.function import proj, embed
from doufo.tensor import Vector
from doufo.tensor import all_close
import pytest

@pytest.mark.parametrize('v,n,expect', [
    ([1.0, 1.0, 0.0], [1.0, 0.0, 0.0], Vector([1.0, 0.0])),
    ([1.0, 2.0, 3.0], [1.0, 0.0, 0.0], Vector([2.0, 3.0]))
])
def test_proj(v, n, expect):
    assert all_close(proj(v, n), expect)


@pytest.mark.parametrize('v,n,expect', [
    ([1.0, 0.0], [1.0, 0.0, 0.0], Vector([0.0, 1.0, 0.0])),
    ([0.0, 1.0], [1.0, 0.0, 0.0], Vector([0.0, 0.0, 1.0])),
    ([1.0, 0.0], [0.0, 1.0, 0.0], Vector([0.0, 0.0, 1.0])),
    ([0.0, 1.0], [0.0, 1.0, 0.0], Vector([1.0, 0.0, 0.0])),
    ([1.0, 0.0], [0.0, 0.0, 1.0], Vector([1.0, 0.0, 0.0])),
    ([0.0, 1.0], [0.0, 0.0, 1.0], Vector([0.0, 1.0, 0.0])),
    ([2.0, 3.0], [1.0, 0.0, 0.0], Vector([0.0, 2.0, 3.0])),
])
def test_embed(v, n, expect):
    assert all_close(embed(v, n), expect)
