import unittest
from dxl.shape.data import Axis3
import numpy as np


class TestAxis(unittest.TestCase):
    def test_construction(self):
        ax = Axis3([1.0, 0.0, 0.0])
        self.assertEqual(ax.normal.x, 1.0)
        self.assertEqual(ax.normal.z, 0.0)
