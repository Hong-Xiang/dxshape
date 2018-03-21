import unittest
from dxl.shape.utils.angle import *
from dxl.shape.utils.vector import Vector3
import numpy as np

AXIS3_VECTORS = np.array([[0., 0., 1.],
                          [1., 0., 0.],
                          [0., 1., 0.],
                          [-1., 0., 0.],
                          [0., -1., 0.],
                          [0., 0., -1.]])

THETA3 = [0., np.pi / 2., np.pi / 2., np.pi / 2., np.pi / 2., np.pi]
PHI3 = [0., 0., np.pi / 2., np.pi, np.pi * 2. / 3., 0.]


class TestSolidAngle(unittest.TestCase):

    def test_theta(self):
        for i in range(AXIS3_VECTORS.shape[0]):
            v = AXIS3_VECTORS[i, :]
            sa = SolidAngle.from_direction_vector(Vector3(v))
            self.assertAlmostEqual(sa.theta(), THETA3[i])
