import unittest

from dxl.shape.rotation.matrix import *
from dxl.shape.utils.vector import Vector3
from dxl.shape.utils.axes import Axis3, AXIS3_X

import numpy as np


class TestAxisToZ(unittest.TestCase):
    def test_x_axis(self):
        v = Vector3([1., 0., 0.])
        ax = Axis3(v)
        rot = axis_to_z(ax)
        np.testing.assert_array_almost_equal(rot,
                                             np.array([[0., 0., 1.],
                                                       [0., 1., 0.],
                                                       [-1., 0., 0.]]))
