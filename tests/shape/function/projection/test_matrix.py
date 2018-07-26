import unittest
from dxl.shape.function.projection import embed2to3, proj3to2
from dxl.function.tensor import all_close
from dxl.shape.data import Matrix
import numpy as np
import pytest


@pytest.mark.parametrize('n, expect', [
    ([1.0, 0.0, 0.0], Matrix([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])),
    ([0.0, 1.0, 0.0], Matrix([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])),
    ([0.0, 0.0, 1.0], Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])),
])
def test_proj3to2(n, expect):
    assert all_close(proj3to2(n), expect)

@pytest.mark.parametrize('n, expect', [
    ([1.0, 0.0, 0.0], Matrix([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])),
    ([0.0, 1.0, 0.0], Matrix([[1.0, 0.0], [0.0, 0.0], [0.0, 1.0]])),
    ([0.0, 0.0, 1.0], Matrix([[1.0, 0.0], [1.0, 0.0], [0.0, 0.0]])),
])
def test_embed2to3(n, expect):
    assert all_close(proj3to2(n), expect)



