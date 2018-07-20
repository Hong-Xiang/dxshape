from .base import Entity
#from .point import Point
#from ..utils.angle import AngleBase, SolidAngle
from ..rotation.matrix import axis_to_z
#, z_to_axis, axis_to_axis
#from .axis import Axis, AXIS3_Z
import numpy as np
#from typing import NamedTuple
import math

class Box(Entity):
    __slot__ = ['origin', 'shape','normal']
    def __init__(self, 
                 shape: np.ndarray,
                 origin: np.ndarray = None,  
                 normal: np.ndarray = None):
        self.shape = shape
        if origin is None:
            origin = np.array([0.0, 0.0, 0.0])
        self.origin = origin
        if normal is None:
            normal = np.array([0.0, 0.0, 1.0])
        self.normal = normal

    def _rotate_on_direction(self, direction, theta):
        p_origin = Point(self.origin)
        p_normal = Point(self.normal)
        return self.replace(origin = p_origin._rotate_on_direction(direction, theta).origin,
                            normal = p_normal._rotate_on_direction(direction, theta).normal)
           
    def is_collision(self, p: 'Entity') -> bool:
        p_tran = p.translate(self.origin)
        rot_matrix = axis_to_z(self.normal)
        p_tran_rot = np.dot(rot_matrix, p_tran.origin)
        if ((p_tran_rot[0] <= 0.5*self.shape[0] or p_tran_rot[0] >= -0.5*self.shape[0]) and 
            (p_tran_rot[1] <= 0.5*self.shape[1] or p_tran_rot[1] >= -0.5*self.shape[1]) and 
            (p_tran_rot[2] <= 0.5*self.shape[2] or p_tran_rot[2] >= -0.5*self.shape[2])):
            return True
        else:
            return False

            

        
