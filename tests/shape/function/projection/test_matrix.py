import unittest
from dxl.shape.function.projection import embed2to3, project3to2
from dxl.function.tensor import all_close
from dxl.shape.data import AXIS3_X, AXIS3_Y, AXIS3_Z, Vector
import numpy as np
import pytest


class TestProjection3to2(unittest.TestCase):
    def test_x(self):
        v = project3to2(AXIS3_X.normal) @ Vector(np.arange(3))
        assert all_close(v, Vector([1., 2.]))

    def test_y(self):
        p = project3to2(AXIS3_Y.normal) @ Vector(np.arange(3))
        assert all_close(p, Vector([0., 2.]))

    def test_z(self):
        p = project3to2(AXIS3_Z.normal) @ Vector(np.arange(3))
        assert all_close(p, Vector([0., 1.]))


class TestProjection2to3(unittest.TestCase):
    def test_x(self):
        p = embed2to3(AXIS3_X.normal) @ Vector([1.0, 1.0])
        assert all_close(p, Vector([0., 1., 1.]))

    def test_y(self):
        p = embed2to3(AXIS3_Y.normal) @ Vector([1.0, 1.0])
        assert all_close(p, Vector([1., 0., 1.]))

    def test_z(self):
        p = embed2to3(AXIS3_Z.normal) @ Vector([1.0, 1.0])
        assert all_close(p, Vector([1., 1., 0.]))
