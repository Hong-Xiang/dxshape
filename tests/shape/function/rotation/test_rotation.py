import unittest
from dxl.shape.function.rotation.matrix import axis_to_axis, axis_to_z, z_to_axis, rotate2, rotate3
from dxl.shape.data import Axis, AXIS3_X, AXIS3_Y, AXIS3_Z
from doufo.tensor import Vector
from doufo.tensor import all_close
from doufo import List
import itertools
#from dxl.shape.utils.vector import Vector3
#from dxl.shape.utils.axes import Axis3, AXIS3_X, AXIS3_Z
import pytest
import math
import numpy as np

RANDOM_VECTORS = List([[0.40980446,  0.56395448, -0.71694885],
                       [-0.89215861, -0.28282346,  0.35222706],
                       [0.97295371,  0.16958264, -0.15685284],
                       [-0.79043812, -0.48951234,  0.36821901],
                       [-0.79298153, -0.55981545,  0.24038919],
                       [0.88280373,  0.38964822, -0.26235821],
                       [-0.65851061,  0.1799812,  0.73073288],
                       [0.3341779, -0.69191882, -0.63997928],
                       [-0.34021323, -0.75627046, -0.55884698],
                       [-0.0612565, -0.29257462, -0.95427865]]).fmap(Vector)

AXIS_VECTORS = List([[0., 0., 1.],
                     [1., 0., 0.],
                     [0., 1., 0.],
                     [-1., 0., 0.],
                     [0., -1., 0.],
                     [0., 0., -1.]]).fmap(Vector)

POINT_VECTORS = List([[1.0, 2.0, 0.0],
                      [-2.0, 1.0, 0.0],
                      [1.0, 0.0, 2.0],
                      [0.0, 2.0, -1.0]]).fmap(Vector)

class TestRotate:
    def test_rotate2(self):
        rot = rotate2(math.pi / 3)
        assert all_close(rot, [[0.5, -math.sqrt(3)/2], [math.sqrt(3)/2, 0.5]])

    @pytest.mark.parametrize('v, expect', list(zip(AXIS_VECTORS[0:3], POINT_VECTORS[1:4])))
    # @pytest.mark.parametrize('v, expect', [AXIS_VECTORS[0:3], POINT_VECTORS[1:4]])
    def test_rotate3(self, v, expect):
        rot = rotate3(math.pi/2, v)
        assert all_close(rot@POINT_VECTORS[0], expect) 


class TestAxisToZ:
    @pytest.mark.parametrize('v', AXIS_VECTORS)
    def test_axis_vectors(self, v):
        rot = axis_to_z(v)
        assert all_close(rot@v, AXIS3_Z.normal)

    @pytest.mark.parametrize('v', AXIS_VECTORS)
    def test_random_vectors(self, v):
        rot = axis_to_z(v)
        assert all_close(rot@v, AXIS3_Z.normal)


class TestZToAxis:

    @pytest.mark.parametrize('v', AXIS_VECTORS)
    def test_axis_vectors(self, v):
        rot = z_to_axis(Vector(v))
        assert all_close(rot@(AXIS3_Z.normal), v)

    @pytest.mark.parametrize('v', RANDOM_VECTORS)
    def test_random_vectors(self, v):
        rot = z_to_axis(Vector(v))
        assert all_close(rot@(AXIS3_Z.normal), v)


class TestAxisToAxis:
    @pytest.mark.parametrize('src,tar', List(itertools.product(RANDOM_VECTORS, AXIS_VECTORS)))
    def test_random_axis(self, src, tar):
        # data = np.concatenate([RANDOM_VECTORS, AXIS_VECTORS])
        # axis = [Axis(np.array(data[i, :]))
                # for i in range(data.shape[0])]
        # for src in axis:
            # for tar in axis:
                # v_tar = tar.normal
                # v_src = src.normal
                # print(type(v_src))
                # print(type(v_tar))
        m = axis_to_axis(src, tar)
        det = np.linalg.det(m.unbox())
        assert abs(det) == pytest.approx(1.0)
        assert all_close(m@src, tar)


if __name__ == '__main__':
    unittest.main()
