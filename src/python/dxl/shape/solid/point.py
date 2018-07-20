from .base import Entity
#from .box import Box
#from .axis import Axis, AXIS3_Z
from ..rotation.matrix import rotate2, rotate3, axis_to_z, z_to_axis
import numpy as np

__all__ = ["Point"]


class Point(Entity):
    __slot__ = ['origin']
    def __init__(self, origin):
        self.origin = origin
    
    def _rotate_on_direction(self, direction: np.ndarray, theta: float):
        if self.ndim == 2:
            rot_matrix = rotate2(theta)
            return self.replace(origin = np.dot(rot_matrix, self.origin))
        elif self.ndim ==3:
            rot_matrix1 = axis_to_z(direction)
            rot_matrix2 = rotate3(theta, 'AXIS3_Z')
            rot_matrix3 = z_to_axis(direction)
            return self.replace(origin = np.dot(rot_matrix3,np.dot(rot_matrix2,np.dot(rot_matrix1, self.origin))))

    def is_in(self, s:'Entity') -> bool:
       return s.is_collision(self)

# class Origin(Point):
#     def __init__(self, ndim=None):
#         from ..utils import get_default_space
#         if ndim is None:
#             ndim = get_default_space().ndim
#         super().__init__(VectorLowDim([0.0] * ndim))
