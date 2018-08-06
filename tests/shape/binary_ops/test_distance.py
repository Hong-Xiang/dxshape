import unittest
import contextlib
# from dxl.shape.binary_ops.distance import distance_between

import pytest



@pytest.mark.skip("Not impleted yet.")
@contextlib.contextmanager
def discussion_in_R3():
    from dxl.shape import default_space, R3
    with default_space(R3):
        yield


@pytest.mark.skip("Not impleted yet.")
class TestDistanceBetween(unittest.TestCase):
    def test_distance_between_points_in_R3(self):
        from dxl.shape import Origin, UnitVector
        with discussion_in_R3():
            p0, p1 = Origin(), UnitVector()
            self.assertAlmostEqual(distance_between(p0, p1), 1.0)

    def test_distance_between_paralle_lines_in_R3(self):
        from dxl.shape import Line, Origin, UnitVector, Vector
        with discussion_in_R3():
            p0, p1 = Origin(), UnitVector()
            l0 = Line(p0, p1)
            offset = Vector([0.0, 1.0, 2.0])
            l1 = Line(p0 + offset, p1 + offset)
            self.assertAlmostEqual(distance_between(l0, l1), offset.norm())
