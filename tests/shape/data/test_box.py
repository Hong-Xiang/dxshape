import unittest
import numpy as np
import math
from dxl.shape.data import Box, Point, Axis, Entity
# from dxl.shape.data.point import Point
# from dxl.shape.data.axis import Axis
# from dxl.shape.data.base import Entity
from doufo.tensor import all_close, Vector

class TestBox(unittest.TestCase):
    def test_init(self):
        b1 = Box([10, 10, 10], [1.0, 2.0, 0.0], [0, 1, 0])
        b2 = Box([10, 10, 10])
        assert all_close(b1.shape, [10, 10, 10])
        assert all_close(b1.origin, [1.0, 2.0, 0.0])
        assert all_close(b1.normal, [0, 1, 0])
        assert all_close(b1.shape, [10, 10, 10])
        assert all_close(b2.origin, [0, 0, 0])
        assert all_close(b2.normal, [0, 0, 1])


    # def test__rotate_on_direction(self):
    #     b = Box([10, 10, 10], [1.0, 2.0, 0.0], [0, 1, 0])
    #     direction_x = np.array([1.0, 0.0, 0.0])
    #     direction_y = np.array([0.0, 1.0, 0.0])
    #     direction_z = np.array([0.0, 0.0, 1.0])
    #     theta = math.pi / 2
    #     b_rot_x = b._rotate_on_direction(direction_x, theta)
    #     b_rot_y = b._rotate_on_direction(direction_y, theta)
    #     b_rot_z = b._rotate_on_direction(direction_z, theta)
    #     self.assertEqual(b_rot_x, Box(np.array([10, 10, 10]), np.array([1.0, 0.0, 2.0]), np.array([0.0, 0.0, 1.0])))
    #     self.assertEqual(b_rot_y, Box([10, 10, 10], [0.0, 2.0, -1.0], [0.0, 1.0, 0.0]))
    #     self.assertEqual(b_rot_z, Box([10, 10, 10], [-2.0, 1.0, 0.0], [-1.0, 0.0, 0.0]))




    def test_rotate(self):
        b = Box([10, 10, 10], [1.0, 2.0, 0.0], [0, 1, 0])
        axis = Axis(normal = Vector([-1.0, 0.0, 0.0]), origin = Vector([0.0, 1.0, 0.0]))
        theta = math.pi/2
        b_rotate = b.rotate(axis, theta)
        self.assertEqual(b_rotate, Box([10, 10, 10], [1.0, 1.0, -1.0], [0.0, 0.0, -1.0]))
    #     # np.testing.assert_array_almost_equal(b_rotate.shape, [10,10,10])
        # np.testing.assert_array_almost_equal(b_rotate.normal, [0.0, 0.0, -1.0])
    
    def test_is_collision(self):
        p1 = Point([0, 0, 0])
        p2 = Point([20, 0, 0])
        b = Box([10, 10, 10], [0, 0, 0], [0, 0, 1])
        self.assertIs(b.is_collision(p1), True) 
        self.assertIs(b.is_collision(p2), False)

if __name__ == "__main__":
    unittest.main()