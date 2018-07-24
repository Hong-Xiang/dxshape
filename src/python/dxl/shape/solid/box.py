from .base import Entity
import numpy as np
import math

class Box(Entity):
    __slot__ = ['shape', 'origin', 'normal']
    def __init__(self, 
                 shape: np.ndarray,
                 origin: np.ndarray = None,  
                 normal: np.ndarray = None):
        if isinstance(shape, (list, tuple)):
            shape = np.asarray(shape)
        self.shape = shape
        if origin is None:
            origin = np.array([0.0, 0.0, 0.0])
        if isinstance(origin, (list, tuple)):
            origin = np.asarray(origin)
        self.origin = origin
        if normal is None:
            normal = np.array([0.0, 0.0, 1.0])
        if isinstance(normal, (list, tuple)):
            normal = np.asarray(normal)
        self.normal = normal

    def _rotate_on_direction(self, direction, theta):
        from dxl.shape.solid.point import Point
        p_origin = Point(self.origin)
        p_normal = Point(self.normal)
        return self.replace(origin = p_origin._rotate_on_direction(direction, theta).origin,
                            normal = p_normal._rotate_on_direction(direction, theta).origin)
           
    def is_collision(self, p: 'Entity') -> bool:
        from dxl.shape.solid.axis import Axis
        from dxl.shape.rotation.matrix import axis_to_z
        p_tran = p.translate(self.origin)
        rot_matrix = axis_to_z(Axis(self.normal))
        p_tran_rot = np.dot(rot_matrix, p_tran.origin)
        for i in range(3):
            if any(abs(p_tran_rot) > self.shape[i] / 2):
                return False
        return True

    def __eq__(self, b):
        if not isinstance(b, Box):
            return False
        return np.allclose(self.shape, b.shape) and np.allclose(self.origin, b.origin) and np.allclose(self.normal, b.normal)

    # def __sub__(self, b):
    #     return self.replace(shape = self.shape- np.array(b.shape),
    #                         origin = self.origin- np.array(b.origin), 
    #                         normal = self.normal- np.array(b.normal))

        # if ((p_tran_rot[0] <= 0.5*self.shape[0] or p_tran_rot[0] >= -0.5*self.shape[0]) and 
        #     (p_tran_rot[1] <= 0.5*self.shape[1] or p_tran_rot[1] >= -0.5*self.shape[1]) and 
        #     (p_tran_rot[2] <= 0.5*self.shape[2] or p_tran_rot[2] >= -0.5*self.shape[2])):
        #     return True
        # else:
        #     return False

    

            

        
