import unittest
import numpy as np
import math
from dxl.shape.solid.box import Box
from dxl.shape.solid.point import Point
from dxl.shape.solid.axis import Axis
from dxl.shape.histogram.histo_point_box import histo_points_to_box

def test_histo_point_box_1_0(self):
    p1 = Point([[1,2,5]])
    p2 = Point([[2,2,6]])
    b = Box([10,10,10],[0,0,0],[0,0,1])
    h = histo_points_to_box(points= [p1, p2],
                            box= b,
                            bias=[2,2,2],
                            weights=None)
    np.testing.assert_allclose(np.nonzero(h), np.array([3,3,0]))
    self.assert_allclose(h(np.nonzero(h)), 1.0)

def test_histo_point_box_1_1(self):
    p1 = Point([[1,2,5]])
    p2 = Point([[3,5,1]])
    b = Box([10,10,10],[0,0,0],[0,0,1])
    h = histo_points_to_box(points= [p1, p2],
                            box= b,
                            bias=[2,2,2],
                            weights=None)
    np.testing.assert_allclose(np.nonzero(h), np.array([[3,3,0],[4,5,3]]))
    self.assert_allclose(h(np.nonzero(h)[0]), 1.0)
    self.assert_allclose(h(np.nonzero(h)[1]), 1.0)

def test_histo_point_box_0_0(self):
    p1 = Point([[6,7,8]])
    p2 = Point([[4,5,9]])
    b = Box([10,10,10],[0,0,0],[0,0,1])
    h = histo_points_to_box(points= [p1, p2],
                            box= b,
                            bias=[2,2,2],
                            weights=None)
    np.testing.assert_allclose(np.nonzero(h), None)
    

if __name__ == '__main__':
    unittest.main()

