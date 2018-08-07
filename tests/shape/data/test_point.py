import unittest
import numpy as np
import math
from dxl.shape.data import Point, Box, Vector
from dxl.shape.data import AXIS3_X, AXIS3_Y, AXIS3_Z, Axis, AXES3
from dxl.shape.function import testing
from doufo.tensor import all_close
import pytest


class TestPoint(unittest.TestCase):
    def test_init(self):
        p = Point([1.0, 2.0, 0.0])
        assert isinstance(p.origin, Vector)
        assert all_close(p.origin, [1.0, 2.0, 0.0])

    def test_ndim(self):
        p = Point(origin=Vector([1.0, 2.0, 0.0]))
        self.assertEqual(p.ndim, 3)

    def test_translate(self):
        p = Point(origin=[1.0, 2.0, 0.0])
        assert testing.all_close(p.translate(-Vector([1.0, 1.0, 3.0])),
                                 Point([0.0, 1.0, -3.0]))

    # @pytest.mark.skip('maybe not needed')
    # def test__rotate_on_direction(self):
    #     p = Point(origin=Vector([1.0, 2.0, 0.0]))
    #     direction_x = Vector([1.0, 0.0, 0.0])
    #     direction_y = Vector([0.0, 1.0, 0.0])
    #     direction_z = Vector([0.0, 0.0, 1.0])
    #     theta = math.pi / 2
    #     # p_rot_x = p._rotate_on_direction(direction_x, theta)
    #     # p_rot_y = p._rotate_on_direction(direction_y, theta)
    #     # p_rot_z = p._rotate_on_direction(direction_z, theta)
    #     self.assertAlmostEquals(p._rotate_on_direction(
    #         direction_x, theta), Point(Vector([1.0, 0.0, 2.0])))
    #     self.assertAlmostEquals(p._rotate_on_direction(
    #         direction_y, theta), Point(Vector([0.0, 2.0, -1.0])))
    #     self.assertAlmostEquals(p._rotate_on_direction(
    #         direction_z, theta), Point(Vector([-2.0, 1.0, 0.0])))

    def test_rotate_x(self):
        p = Point(origin=Vector([0.0, 2.0, 0.0]))
        assert testing.all_close(p.rotate(AXES3.x, math.pi / 2),
                                 Point([0.0, 0.0, 2.0]))

    def test_rotate_neg_x(self):
        p = Point(origin=Vector([0.0, 2.0, 0.0]))
        axis = Axis(normal=[-1.0, 0.0, 0.0])
        assert testing.all_close(p.rotate(axis, math.pi / 2),
                                 Point([0.0, 0.0, -2.0]))

    def test_rotate_not_origin(self):
        p = Point(origin=Vector([0.0, 2.0, 0.0]))
        axis = Axis(normal=[0.0, 0.0, 1.0], origin=[0.0, 1.0, 0.0])
        assert testing.all_close(p.rotate(axis, math.pi / 2),
                                 Point([-1.0, 1.0, 0.0]))

    def test_is_in(self):
        p1 = Point([0, 0, 0])
        p2 = Point([20, 0, 0])
        b = Box([10, 10, 10], [0, 0, 0], [0, 0, 1])
        self.assertIs(p1.is_in(b), True)
        self.assertIs(p2.is_in(b), False)


if __name__ == "__main__":
    unittest.main()
