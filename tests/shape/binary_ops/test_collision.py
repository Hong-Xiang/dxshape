from dxl.shape.data import Point, Box
from dxl.shape.function import is_collision
import unittest

def test_collision_in():
    p = Point([0, 0, 0])
    b = Box([10, 10, 10], [0, 0, 0], [0, 0, 1])
    assert is_collision(p, b) 

def test_collision_not_in():
    p = Point([20, 0, 0])
    b = Box([10, 10, 10], [0, 0, 0], [0, 0, 1])
    assert not is_collision(p, b) 

if __name__ == '__main__':
    unittest.main()