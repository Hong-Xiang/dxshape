from functools import singledispatch
from dxl.shape.data import  Axis, AXIS3_X, AXIS3_Y, AXIS3_Z, Quaternion, make_rotate_matrix
from doufo.tensor import Vector, Matrix, transpose, all_close

import numpy as np
import math


__all__ = ['rotate2', 'rotate3', 'axis_to_z', 'z_to_axis', 'axis_to_axis']


def rotate2(theta: float) -> Matrix:
    """
    Parameters:

    - `theta`: rotation angle in radians
    """
    c, s = np.cos(theta), np.sin(theta)
    return Matrix([[c, -s], [s, c]])


# def rotate3(theta: float, n: Vector) -> Matrix:
#     """
#     Rotation alone specific axis.

#     Note `axis` must be one of `AXIS3_X`, `AXIS3_Y` and `AXIS3_Z`
#     """
#     from ..projection import embed2to3, proj3to2
#     # FIXME clear impl
#     if isinstance(n, Axis):
#         n = n.normal
#     rotate_matrix = embed2to3(n)@rotate2(theta)@proj3to2(n)
#     identity_matrix = np.zeros([3, 3])
#     identity_dim = axis_dim_id(n)
#     identity_matrix[identity_dim, identity_dim] = 1.0
#     identity_matrix = Matrix(identity_matrix)
#     result = rotate_matrix + identity_matrix
#     return result

def rotate3(theta: float, n: Vector) -> Matrix:
    q = Quaternion(theta, n.x, n.y, n.z)
    identity_matrix = Matrix(make_rotate_matrix(q))
    return identity_matrix





def axis_dim_id(a):
    if all_close(a, AXIS3_X.normal):
        return 0
    if all_close(a, AXIS3_Y.normal):
        return 1
    if all_close(a, AXIS3_Z.normal):
        return 2
    raise ValueError(f"Invalid axis for axis dim id: {a}")


def axis_to_z(axis: Vector) -> Matrix:
    """
    Rotation matrix rotate given axis to normal z axis
    """
    rot_y, rot_z = get_rot_yz(axis)
    return rotate3(-rot_y, AXIS3_Y.normal)@rotate3(-rot_z, AXIS3_Z.normal)


def z_to_axis(axis: Vector):
    """
    rotation matrix which rotate normal z axis to given axis
    """
    rot_y, rot_z = get_rot_yz(axis)
    return rotate3(rot_z, AXIS3_Z.normal)@rotate3(rot_y, AXIS3_Y.normal)

def get_rot_yz(axis):
    axis = Vector(axis)
    # rot_y = math.acos(axis.z)
    # rot_z = math.atan2(axis.y, axis.x)
    rot_y = math.acos(axis[2])
    rot_z = math.atan2(axis[1], axis[0])
    return rot_y, rot_z


def axis_to_axis(source, target):
    """
    Rotation matrix which rotate source axis to target axis.
    Implemented by firstly roteta source axis to `AXES3_STD.z`, and then rotate
    `AXES3_STD.z` to target axis.
    """
    source, target = Vector(source), Vector(target)
    # source, target = source.unbox(), target.unbox()
    return z_to_axis(target)@axis_to_z(source)
