import unittest
from dxl.shape.projection import *
from dxl.shape.utils.axes import AXIS3_X, AXIS3_Y, AXIS3_Z
import numpy as np
import pytest


class TestProjection3to2(unittest.TestCase):
    def test_x(self):
        v = np.arange(3)
        p = projection_3to2(AXIS3_X) @ v
        self.assertTrue(np.array_equal(p, np.array([1., 2.])))


class TestProjectionGeneral(unittest.TestCase):
    @pytest.mark.skip('not implemented yet.')
    def test_interface(self):
        from dxl.shape import Line, R3, R2, project, Origin, UnitVector
        l = Line(Origin(3), UnitVector(3))
        lp = project(l).to(R2())
        # TODO: fix expect output
        assert lp == Line(Origin(2), UnitVector(2))
