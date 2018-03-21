import unittest
from dxl.shape.utils.vector import *

class TestVector3(unittest.TestCase):
    def test_dim(self):
        v = Vector3([1., 0., 0.])
        self.assertEqual(v.dim(), 3)
    
    def test_xyz(self):
        v = Vector3([1., 2., 3.])
        self.assertEqual(v.x(), 1.)
        self.assertEqual(v.y(), 2.)
        self.assertEqual(v.z(), 3.)

