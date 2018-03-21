import numpy as np
from ..utils.axes import Axes3, Axis3, AXIS3_X, AXIS3_Y, AXIS3_Z
from ..projection import projection_2to3
import math


def radians3(r: float, axis: Axis3):
    """
    Rotation alone specific axis.

    Note `axis` must be one of `AXIS3_X`, `AXIS3_Y` and `AXIS3_Z`
    """
    return projection_2to3(axis)@np.radians(r)


def axis_to_z(axis: Axis3) -> np.ndarray:
    """
    Rotation matrix rotate given axis to normal z axis
    """
    rad_y = math.asin(axis.direction_vector().z())
    rad_z = math.atan2(axis.direction_vector().y(),
                       axis.direction_vector().x())
    return radians3(-rad_z, AXIS3_Z)@radians3(-rad_y, AXIS3_Y)


def z_to_axis(axes: Axes3):
    """
    rotation matrix which rotate normal z axis to z axis of given axes
    """


def axes_to_axes(source, target):
    """
    Rotation matrix which rotate z axis of source axes to z axis of target axes.
    Implemented by firstly roteta source axes to `AXES3_STD.z`, and then rotate
    `AXES3_STD.z` to target axis.
    """
    return axes_to_z(source) @ z_to_axes(target)
