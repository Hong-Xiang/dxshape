import unittest
import numpy as np
import math
from dxl.shape.data.box import Box
from dxl.shape.data.point import Point
from dxl.shape.data.axis import Axis
from dxl.shape.histogram.histo_point_box import histo_points_to_box
from dxl.data.tensor import Vector, Tensor
from dxl.function.tensor import all_close
import pytest

class TestHistoPointBox(unittest.TestCase):
    def test_histo_point_box_1_0(self):
        p1 = Point([1,2,4])
        p2 = Point([2,2,6])
        b = Box([10,10,10],[0,0,0],[0,0,1])
        p_index, h = histo_points_to_box(points= [p1, p2],
                                         box= b,
                                         grid=[5,5,5],
                                         weights=None)
        expect = Tensor(np.zeros([5,5,5]))
        expect[3,3,0] = 1
        assert all_close(h, expect)

    def test_histo_point_box_1_1(self):
        p1 = Point([1,2,4])
        p2 = Point([3,4,1])
        b = Box([10,10,10],[0,0,0],[0,0,1])
        p_index, h = histo_points_to_box(points= [p1, p2],
                                         box= b,
                                         grid=[5,5,5],
                                         weights=None)
        expect = Tensor(np.zeros([5,5,5]))
        expect[3,3,0] = 1
        expect[4,4,1] = 1
        assert all_close(h, expect)

    def test_histo_point_box_0_0(self):
        p1 = Point([6,7,8])
        p2 = Point([4,5,9])
        b = Box([10,10,10],[0,0,0],[0,0,1])
        p_index, h = histo_points_to_box(points= [p1, p2],
                                         box= b,
                                         grid=[5,5,5],
                                         weights=None)
        expect = Tensor(np.zeros([5,5,5]))
        assert all_close(h, expect)
    

if __name__ == '__main__':
    unittest.main()

