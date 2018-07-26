import unittest
from dxl.shape.function.projection import project2to3, project3to2
from dxl.function.tensor import all_close
from dxl.shape.data import AXIS3_X, AXIS3_Y, AXIS3_Z, Vector
import numpy as np
import pytest


class TestProjection3to2(unittest.TestCase):
    def test_x(self):
        v = project3to2(Vector([1.0, 2.0, 3.0]), [1.0, 0.0, 0.0])
        assert all_close(v, Vector([1., 2.]))

    def test_y(self):
        v = np.arange(3)
        p = project3to2(AXIS3_Y) @ v
        self.assertTrue(np.array_equal(p, np.array([0., 2.])))

    def test_z(self):
        v = np.arange(3)
        p = project3to2(AXIS3_Z) @ v
        self.assertTrue(np.array_equal(p, np.array([0., 1.])))


class TestProjection2to3(unittest.TestCase):
    def test_x(self):
        v = np.array([1., 1.])
        p = project2to3(AXIS3_X) @ v
        self.assertTrue(np.array_equal(p, np.array([0., 1., 1.])))

    def test_y(self):
        v = np.array([1., 1.])
        p = project2to3(AXIS3_Y.normal) @ v
        self.assertTrue(np.array_equal(p, np.array([1., 0., 1.])))

    def test_z(self):
        v = np.array([1., 1.])
        p = project2to3(AXIS3_Z.normal) @ v
        self.assertTrue(np.array_equal(p, np.array([1., 1., 0.])))


# class TestProjectionGeneral(unittest.TestCase):
#     @pytest.mark.skip('not implemented yet.')
#     def test_interface(self):
#         from dxl.shape import Line, R3, R2, project, Origin, UnitVector
#         l = Line(Origin(3), UnitVector(3))
#         lp = project(l).to(R2())
#         # TODO: fix expect output
#         assert lp == Line(Origin(2), UnitVector(2))


if __name__ == '__main__':
    unittest.main()
