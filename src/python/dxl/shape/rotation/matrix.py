import numpy as np
from ..solid.axis import Axis, AXIS3_X, AXIS3_Y, AXIS3_Z
from ..projection import projection_2to3, projection_3to2
import math


def rotate2(theta: float):
    """
    Parameters:

    - `theta`: rotation angle in radians
    """
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


def rotate3(theta: float, axis):
    """
    Rotation alone specific axis.

    Note `axis` must be one of `AXIS3_X`, `AXIS3_Y` and `AXIS3_Z`
    """
    rotate_matrix = projection_2to3(axis)@rotate2(theta)@projection_3to2(axis)
    if axis == 'AXIS3_Y':
        rotate_matrix = np.transpose(rotate_matrix)
    #print(rotate_matrix)
    identity_matrix = np.zeros([3, 3])
    identity_dim = {'AXIS3_X': 0, 'AXIS3_Y': 1, 'AXIS3_Z': 2}[axis]
    identity_matrix[identity_dim, identity_dim] = 1.
    return rotate_matrix + identity_matrix


def axis_to_z(axis: Axis) -> np.ndarray:
    """
    Rotation matrix rotate given axis to normal z axis
    """
    axis_z = axis.direction_vector[2]
    rot_y = math.acos(axis_z)
    rot_z = math.atan2(axis.direction_vector[1],
                       axis.direction_vector[0])
    return rotate3(-rot_y, 'AXIS3_Y')@rotate3(-rot_z, 'AXIS3_Z')


def z_to_axis(axis: Axis):
    """
    rotation matrix which rotate normal z axis to given axis
    """
    axis_z = axis.direction_vector[2]
    rot_y = math.acos(axis_z)
    rot_z = math.atan2(axis.direction_vector[1],
                       axis.direction_vector[0])
    return rotate3(rot_z, 'AXIS3_Z')@rotate3(rot_y, 'AXIS3_Y')


def axis_to_axis(source, target):
    """
    Rotation matrix which rotate source axis to target axis.
    Implemented by firstly roteta source axis to `AXES3_STD.z`, and then rotate
    `AXES3_STD.z` to target axis.
    """
    return z_to_axis(target)@axis_to_z(source)
