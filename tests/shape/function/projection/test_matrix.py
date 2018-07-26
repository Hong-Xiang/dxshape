import unittest
from dxl.shape.function.projection import embed2to3, proj3to2
from dxl.function.tensor import all_close
from dxl.shape.data import Matrix, Vector
import numpy as np
import pytest


@pytest.mark.parametrize('n, expect', [
    ([1.0, 0.0, 0.0], Matrix([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])),
    ([0.0, 1.0, 0.0], Matrix([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0]])),
    ([0.0, 0.0, 1.0], Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])),
])
def test_proj3to2(n, expect):
    assert all_close(proj3to2(n), expect)


@pytest.mark.parametrize('n, expect', [
    ([1.0, 0.0, 0.0], Matrix([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])),
    ([0.0, 1.0, 0.0], Matrix([[0.0, 1.0], [0.0, 0.0], [1.0, 0.0]])),
    ([0.0, 0.0, 1.0], Matrix([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]])),
])
def test_embed2to3(n, expect):
    assert all_close(embed2to3(n), expect)


@pytest.mark.parametrize('n', [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
])
def test_proj3to2_embed2to3(n):
    print(n)
    assert all_close(proj3to2(n) @ embed2to3(n),
                     Matrix([[1.0, 0.0], [0.0, 1.0]]))


@pytest.mark.parametrize('n,expect', [
    (Vector.one_hot(0, 3), Matrix.eye(3) - Matrix.one_hot(0, 3)),
    (Vector.one_hot(1, 3), Matrix.eye(3) - Matrix.one_hot(1, 3)),
    (Vector.one_hot(2, 3), Matrix.eye(3) - Matrix.one_hot(2, 3)),
])
def test_embed2to3_proj3to2(n, expect):
    assert all_close(embed2to3(n) @ proj3to2(n),
                     expect)
