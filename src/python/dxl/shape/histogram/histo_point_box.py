import numpy as np 
import math
from ..data.box import Box
from ..data.point import Point
from ..data.axis import Axis
from ..function.rotation.matrix import axis_to_z 

def histo_points_to_box(points: list, box: Box, bias: list, weights: list = None):
    """
    bias is the grid size, 
    when weights is none, result is number collection matrix 
    """
    if weights is None:
        weights = [1.0] * len(points)
    else:
        weights = weights
    num = [int(box.shape[i]/bias[i]) for i in range(3)]
    result = np.zeros(num)
    points0 = [Point(axis_to_z(Axis(box.normal)).dot(p.translate(-box.origin).origin)) for p in points]
    for p,w in zip(points0, weights):
        if p.is_in(box) is True:
            ix = int((p.origin[0] + 0.5* box.shape[0]) / bias[0])
            iy = int((p.origin[1] + 0.5* box.shape[1]) / bias[1])
            iz = int((0.5* box.shape[2] - p.origin[2]) / bias[2])
            print([ix, iy, iz])
            result[ix][iy][iz] += w
            print(result[ix][iy][iz])
        else:
            pass
    return result 
