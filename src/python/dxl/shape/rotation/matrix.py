import numpy as np
from ..utils.axes import Axes3, Axis3, AXIS3_X, AXIS3_Y, AXIS3_Z
from ..utils.vector import Vector3
from ..projection import projection_2to3, projection_3to2
import math


def rotate2(theta: float):
    """
    Parameters:

    - `theta`: rotation angle in radians
    """
    c, s = np.cos(theta), np.sin(theta)
    return np.array(((c, -s), (s, c)))


def rotate3(theta: float, axis: Axis3):
    """
    Rotation alone specific axis.

    Note `axis` must be one of `AXIS3_X`, `AXIS3_Y` and `AXIS3_Z`
    """
    rotate_matrix = projection_2to3(axis)@rotate2(theta)@projection_3to2(axis)
    identity_matrix = np.zeros([3, 3])
    identity_dim = {AXIS3_X: 0, AXIS3_Y: 1, AXIS3_Z: 2}[axis]
    identity_matrix[identity_dim, identity_dim] = 1.
    return rotate_matrix + identity_matrix


def axis_to_z(axis: Axis3) -> np.ndarray:
    """
    Rotation matrix rotate given axis to normal z axis
    """
    axis_z = axis.direction_vector().z()
    rot_y = math.acos(axis_z)
    rot_z = math.atan2(axis.direction_vector().y(),
                       axis.direction_vector().x())
    return rotate3(rot_y, AXIS3_Y)@rotate3(-rot_z, AXIS3_Z)


def z_to_axis(axis: Axes3):
    """
    rotation matrix which rotate normal z axis to z axis of given axes
    """
    axis_z = axis.direction_vector().z()
    rot_y = math.acos(axis_z)
    rot_z = math.atan2(axis.direction_vector().y(),
                       axis.direction_vector().x())
    return rotate3(rot_z, AXIS3_Z)@rotate3(-rot_y, AXIS3_Y)


def axis_to_axis(source, target):
    """
    Rotation matrix which rotate z axis of source axes to z axis of target axes.
    Implemented by firstly roteta source axes to `AXES3_STD.z`, and then rotate
    `AXES3_STD.z` to target axis.
    """
    return z_to_axis(target)@axis_to_z(source)