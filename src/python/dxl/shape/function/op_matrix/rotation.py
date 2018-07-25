from functools import singledispatch
from dxl.shape.data import Vector, Axis, Matrix
import numpy as np

from dxl.function.tensor import transpose

import numpy as np
from dxl.shape.data import Axis, AXIS3_X, AXIS3_Y, AXIS3_Z
import math
from dxl.function.tensor import all_close


def rotate2(theta: float) -> Matrix:
    """
    Parameters:

    - `theta`: rotation angle in radians
    """
    c, s = np.cos(theta), np.sin(theta)
    return Matrix([[c, -s], [s, c]])


def rotate3(theta: float, n: Vector) -> Matrix:
    """
    Rotation alone specific axis.

    Note `axis` must be one of `AXIS3_X`, `AXIS3_Y` and `AXIS3_Z`
    """
    from .op_matrix import embed2to3, project3to2
    rotate_matrix = embed2to3(n)@rotate2(theta)@project3to2(n)
    if all_close(n, AXIS3_Y.normal):
        rotate_matrix = transpose(rotate_matrix)
    identity_matrix = np.zeros([3, 3])
    identity_dim = axis_dim_id(axis)
    identity_matrix[identity_dim, identity_dim] = 1.0
    identity_matrix = Matrix(identity_matrix)
    result = rotate_matrix + identity_matrix
    return result


def axis_dim_id(a):
    if all_close(a.normal, AXIS3_X.normal):
        return 0
    if all_close(a.normal, AXIS3_Y.normal):
        return 1
    if all_close(a.normal, AXIS3_Z.normal):
        return 2
    raise ValueError(f"Invalid axis for axis dim id: {a}")


def axis_to_z(axis: Axis) -> Matrix:
    """
    Rotation matrix rotate given axis to normal z axis
    """
    rot_y = math.acos(axis.normal.z)
    rot_z = math.atan2(axis.normal.y, axis.normal.x)
    return rotate3(-rot_y, AXIS3_Y)@rotate3(-rot_z, AXIS3_Z)


def z_to_axis(axis: Axis):
    """
    rotation matrix which rotate normal z axis to given axis
    """
    rot_y = math.acos(axis.normal.z)
    rot_z = math.atan2(axis.normal.y, axis.normal.x)
    return rotate3(rot_z, AXIS3_Z)@rotate3(rot_y, AXIS3_Y)


def axis_to_axis(source, target):
    """
    Rotation matrix which rotate source axis to target axis.
    Implemented by firstly roteta source axis to `AXES3_STD.z`, and then rotate
    `AXES3_STD.z` to target axis.
    """
    return z_to_axis(target)@axis_to_z(source)
