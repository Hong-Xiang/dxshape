from .base import Solid, Shape
from ..utils.axes import Axes, Axis3, AXIS3_Z
from ..utils.vector import VectorLowDim 
from ..rotation.matrix import rotate2, rotate3, axis_to_z, z_to_axis
import numpy as np

__all__ = ["Point"]


class Point(Shape):
    def __init__(self, data: VectorLowDim):
        if isinstance(data, (list, tuple)):
            data = VectorLowDim.from_list(data)
        self._data = data

    def data(self):
        return self._data

    def dim(self):
        return self._data.dim()

    def origin(self):
        return self._data

    def translate(self, v: VectorLowDim) -> 'Point':
        return Point((self.origin() - v))

    def rotate_origin(self, axis: Axes=None, angle: float=None, rotate_matrix: np.array=None):
        if (axis is None) and (angle is None):
            if rotate_matrix.shape[0] is None:
                raise ValueError("rotation matrix is none.")
            elif self.dim() !=rotate_matrix.shape[0]:
                fmt = "Invalid data dimension {} when {} is expected."
                raise ValueError(fmt.format(rotate_matrix.shape[0], self.dim()))
 #           else:
            elif self.dim() == rotate_matrix.shape[0]:
                rotation_matrix = rotate_matrix
                after_point = np.dot(rotation_matrix,self.origin())
        elif (axis is None) and (angle is not None) and (rotate_matrix is None) and (self.dim()==2):
            rotation_matrix=rotate2(angle)
            after_point = np.dot(rotation_matrix,self.origin())
        elif (axis is not None) and (angle is not None) and (rotate_matrix is None) and (self.dim()==3): 
            trans_p=self.translate(axis.origin) 
            rotation_matrix1 = axis_to_z(Axis3(axis.direction_vector))
            rotation_matrix2 = rotate3(theta=angle, axis=AXIS3_Z) 
            rotation_matrix3 = z_to_axis(Axis3(axis.direction_vector))   
            np.array(trans_p._data).shape=(1,3) 
            rotated_point=np.transpose(np.dot(rotation_matrix3,np.dot(rotation_matrix2,np.dot(rotation_matrix1,np.transpose(np.array(trans_p._data))))))
            after_point = rotated_point + np.array(axis.origin.data())
        return Point(VectorLowDim.from_list(after_point))

    def translate_origin(self, v) -> 'Point':
        raise NotImplementedError

    def rotate(self, axis, theta) -> 'Point':
        pass

    def is_in(self, s: Solid) -> bool:
        from dxl.shape.binary_ops import is_collision
        return is_collision(self, s)

    def __sub__(self, v):
        return Point(self._data - v)

    def __mul__(self, v):
        return Point(self.data() * v.data())

    def __getitem__(self, i):
        return self._data[i]

    def __repr__(self):
        return "<Point({})>".format(self.data())


class Origin(Point):
    def __init__(self, ndim=None):
        from ..utils import get_default_space
        if ndim is None:
            ndim = get_default_space().ndim
        super().__init__(VectorLowDim([0.0] * ndim))
