import unittest
from dxl.shape.projection import *
from dxl.shape.utils.axes import AXIS3_X, AXIS3_Y, AXIS3_Z
import numpy as np


class TestProjection3to2(unittest.TestCase):
    def test_x(self):
        v = np.arange(3)
        p = projection_3to2(AXIS3_X)@v
        self.assertTrue(np.array_equal(p,
                                       np.array([1., 2.])))
