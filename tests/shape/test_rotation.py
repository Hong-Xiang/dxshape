import unittest

from dxl.shape.rotation.matrix import *
from dxl.shape.utils.vector import Vector3
from dxl.shape.utils.axes import Axis3, AXIS3_X, AXIS3_Z

import numpy as np

RANDOM_VECTORS = np.array([[0.40980446,  0.56395448, -0.71694885],
                           [-0.89215861, -0.28282346,  0.35222706],
                           [0.97295371,  0.16958264, -0.15685284],
                           [-0.79043812, -0.48951234,  0.36821901],
                           [-0.79298153, -0.55981545,  0.24038919],
                           [0.88280373,  0.38964822, -0.26235821],
                           [-0.65851061,  0.1799812,  0.73073288],
                           [0.3341779, -0.69191882, -0.63997928],
                           [-0.34021323, -0.75627046, -0.55884698],
                           [-0.0612565, -0.29257462, -0.95427865]])

AXIS_VECTORS = np.array([[0., 0., 1.],
                         [1., 0., 0.],
                         [0., 1., 0.],
                         [-1., 0., 0.],
                         [0., -1., 0.],
                         [0., 0., -1.]])


class TestAxisToZ(unittest.TestCase):
    def test_axis_vectors(self):
        for i in range(AXIS_VECTORS.shape[0]):
            v = Vector3(AXIS_VECTORS[i, :])
            ax = Axis3(v)
            rot = axis_to_z(ax)
            np.testing.assert_array_almost_equal(rot@v.data(),
                                                 AXIS3_Z.direction_vector().data())

    def test_random_vectors(self):
        for i in range(RANDOM_VECTORS.shape[0]):
            v = Vector3(RANDOM_VECTORS[i, :])
            ax = Axis3(v)
            rot = axis_to_z(ax)
            np.testing.assert_array_almost_equal(rot@v.data(),
                                                 AXIS3_Z.direction_vector().data())


class TestZToAxis(unittest.TestCase):
    def test_axis_vectors(self):
        for i in range(AXIS_VECTORS.shape[0]):
            v = Vector3(AXIS_VECTORS[i, :])
            ax = Axis3(v)
            rot = z_to_axis(ax)
            np.testing.assert_array_almost_equal(rot@(AXIS3_Z.direction_vector()
                                                      .data()),
                                                 v.data())

    def test_random_vectors(self):
        for i in range(RANDOM_VECTORS.shape[0]):
            v = Vector3(RANDOM_VECTORS[i, :])
            ax = Axis3(v)
            rot = z_to_axis(ax)
            np.testing.assert_array_almost_equal(rot@(AXIS3_Z.direction_vector()
                                                      .data()),
                                                 v.data())


class TestAxisToAxis(unittest.TestCase):
    def test_random_axis(self):
        axis = [Axis3(Vector3(RANDOM_VECTORS[i, :]))
                for i in range(RANDOM_VECTORS.shape[0])]
        for src in axis:
            for tar in axis:
                v_tar = tar.direction_vector().data()
                v_src = src.direction_vector().data()
                m = axis_to_axis(src, tar)
                det = np.linalg.det(m)
                np.testing.assert_almost_equal(abs(det), 1.0)
                np.testing.assert_array_almost_equal(m@v_src, v_tar)
