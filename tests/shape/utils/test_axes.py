import unittest
from dxl.shape.utils.axes import *
from dxl.shape.utils.vector import Vector3
import numpy as np


class TestAxis(unittest.TestCase):
    def test_construction(self):
        v = Vector3([1., 0., 0.])
        ax = Axis3(v)
        self.assertEqual(ax.direction_vector().x(), 1.0)
        self.assertEqual(ax.direction_vector().z(), 0.0)
