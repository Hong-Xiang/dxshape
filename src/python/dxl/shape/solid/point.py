from .base import Entity
import numpy as np

__all__ = ["Point"]


class Point(Entity):
    __slot__ = ['origin']
    def __init__(self, origin):
        if isinstance(origin, (list, tuple)):
            origin = np.asarray(origin)
        self.origin = origin
    
    def _rotate_on_direction(self, direction: np.ndarray, theta: float):
        from dxl.shape.solid.axis import Axis
        from dxl.shape.rotation.matrix import rotate2, rotate3, axis_to_z, z_to_axis
        if self.ndim == 2:
            rot_matrix = rotate2(theta)
            return self.replace(origin = np.dot(rot_matrix, self.origin))
        elif self.ndim ==3:
            rot_matrix1 = axis_to_z(Axis(direction))
            rot_matrix2 = rotate3(theta, 'AXIS3_Z')
            rot_matrix3 = z_to_axis(Axis(direction))
            return self.replace(origin = rot_matrix3.dot(rot_matrix2.dot(rot_matrix1.dot(self.origin))))

    def is_in(self, s:'Entity') -> bool:
       return s.is_collision(self)

    def __eq__(self, p):
        if not isinstance(p, Point):
            return False
        return np.allclose(self.origin, p.origin)
# class Origin(Point):
#     def __init__(self, ndim=None):
#         from ..utils import get_default_space
#         if ndim is None:
#             ndim = get_default_space().ndim
#         super().__init__(VectorLowDim([0.0] * ndim))
