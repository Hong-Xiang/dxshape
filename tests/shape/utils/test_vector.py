import unittest
from dxl.shape.utils.vector import *

class TestVector3(unittest.TestCase):
    def test_dim(self):
        v = Vector3([1., 0., 0.])
        self.assertEqual(v.dim(), 3)

