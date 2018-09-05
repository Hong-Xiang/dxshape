import unittest
import numpy as np
import math
from dxl.shape.data import AXIS3_X, AXIS3_Y, AXIS3_Z, Axis
from doufo.tensor import all_close, Vector


class TestAxis(unittest.TestCase):
    def test_init(self):
        a1 = Axis(normal=Vector([0.0, 1.0, 0.0]), origin=Vector([1.0, 2.0, 0.0]))
        a2 = Axis(normal=Vector([0.0, 1.0, 0.0]))
        assert all_close(a1.normal, Vector([0.0, 1.0, 0.0]))
        assert all_close(a1.origin, Vector([1.0, 2.0, 0.0]))
        assert all_close(a2.normal, Vector([0.0, 1.0, 0.0]))
        assert all_close(a2.origin, Vector([0.0, 0.0, 0.0]))
        self.assertTrue(isinstance(a1, Axis))
        self.assertTrue(isinstance(a2, Axis))

    def test_rotate_on_direction(self):
        a = Axis(normal=Vector([0.0, 1.0, 0.0]), origin=Vector([1.0, 2.0, 0.0]))
        direction_x = Vector([1.0, 0.0, 0.0])
        direction_y = Vector([0.0, 1.0, 0.0])
        direction_z = Vector([0.0, 0.0, 1.0])
        theta = math.pi / 2
        a_rot_x = a.rotate_on_direction(direction_x, theta)
        a_rot_y = a.rotate_on_direction(direction_y, theta)
        a_rot_z = a.rotate_on_direction(direction_z, theta)
        assert all_close(a_rot_x.origin, Vector([1.0, 0.0, 2.0]))
        assert all_close(a_rot_x.normal, Vector([0.0, 0.0, 1.0]))
        assert all_close(a_rot_y.origin, Vector([0.0, 2.0, -1.0]))
        assert all_close(a_rot_y.normal, Vector([0.0, 1.0, 0.0]))
        assert all_close(a_rot_z.origin, Vector([-2.0, 1.0, 0.0]))
        assert all_close(a_rot_z.normal, Vector([-1.0, 0.0, 0.0]))

    def test_construction(self):
        ax = Axis(Vector([1.0, 0.0, 0.0]))
        self.assertEqual(ax.normal.x, 1.0)
        self.assertEqual(ax.normal.z, 0.0)


if __name__ == "__main__":
    unittest.main()
