import unittest
import numpy as np
import math
from dxl.shape.solid.base import NamedTuple, Entity
from dxl.shape.solid.axis import AXIS3_X, AXIS3_Y, AXIS3_Z, Axis

class TestAxis(unittest.TestCase):
    def test_init(self):
        a1 = Axis(direction_vector= [0.0, 1.0, 0.0], origin= [1.0, 2.0, 0.0])
        a2 = Axis(direction_vector= [0.0, 1.0, 0.0])
        np.testing.assert_allclose (a1.direction_vector, [0.0, 1.0, 0.0])
        np.testing.assert_allclose (a1.origin, [1.0, 2.0, 0.0])
        np.testing.assert_allclose (a2.direction_vector, [0.0, 1.0, 0.0])
        np.testing.assert_allclose (a2.origin, [0.0, 0.0, 0.0])
        self.assertTrue(isinstance(a1, Entity))
        self.assertTrue(isinstance(a1, NamedTuple))
        self.assertTrue(isinstance(a2, Entity))
        self.assertTrue(isinstance(a2, NamedTuple))

    def test_rotate_on_direction(self):
        a = Axis(direction_vector= [0.0, 1.0, 0.0], origin= [1.0, 2.0, 0.0])      
        direction_x = np.array([1.0, 0.0, 0.0])
        direction_y = np.array([0.0, 1.0, 0.0])
        direction_z = np.array([0.0, 0.0, 1.0])
        theta = math.pi / 2
        a_rot_x = a._rotate_on_direction(direction_x, theta)
        a_rot_y = a._rotate_on_direction(direction_y, theta)
        a_rot_z = a._rotate_on_direction(direction_z, theta)
        np.testing.assert_array_almost_equal(a_rot_x.origin, [1.0, 0.0, 2.0])
        np.testing.assert_array_almost_equal(a_rot_x.direction_vector, [0.0 ,0.0, 1.0])
        np.testing.assert_array_almost_equal(a_rot_y.origin, [0.0, 2.0, -1.0])
        np.testing.assert_array_almost_equal(a_rot_y.direction_vector, [0.0, 1.0, 0.0])
        np.testing.assert_array_almost_equal(a_rot_z.origin, [-2.0, 1.0, 0.0])
        np.testing.assert_array_almost_equal(a_rot_z.direction_vector, [-1.0, 0.0, 0.0])


   
if __name__ == "__main__":
    unittest.main()