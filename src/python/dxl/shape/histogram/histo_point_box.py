import numpy as np 
import math
import random
from dxl.shape.data.box import Box
from dxl.shape.data.point import Point
from dxl.shape.data.axis import Axis
from dxl.shape.function.box import divide
from doufo.tensor import Tensor, Vector

def histo_points_to_box(points: list, box: Box, grid: list, weights: list = None):
    """
    grid is the grid num, 
    when weights is none, result is number collection matrix 
    """
    if weights is None:
        weights = [1.0] * len(points)
    else:
        weights = weights
    result = np.zeros(grid)
    subbox = divide(box, grid)
    #subbox = [b.translate(b.shape / 2 - box.shape / 2) for b in subbox]
    p_index = list()
    for p, w in zip(points, weights):
        for b in subbox:
            if b.is_collision(p) == True:
                p_index.append(b.origin)
                ix = int(((b.origin.x - box.origin.x) + 0.5* box.shape.x) / b.shape.x)
                iy = int(((b.origin.y - box.origin.y)+ 0.5* box.shape.y) / b.shape.y)
                iz = int((0.5* box.shape.z - (b.origin.z - box.origin.z)) / b.shape.z)
                result[ix, iy, iz] += w
                #print([ix, iy,iz])
    return p_index, Tensor(result)
