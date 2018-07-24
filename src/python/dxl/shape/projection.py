from .solid.axis import Axis, AXIS3_X, AXIS3_Y, AXIS3_Z
import numpy as np

# TODO: move to binary_ops


def projection_3to2(squeeze_axis):
    if not squeeze_axis in ('AXIS3_X', 'AXIS3_Y', 'AXIS3_Z'):
        raise ValueError("Unsupported squeeze axis {}.".format(squeeze_axis))
    if squeeze_axis == 'AXIS3_X':
        return np.array([[0., 1., 0.], [0., 0., 1.]])
    if squeeze_axis == 'AXIS3_Y':
        return np.array([[1., 0., 0.], [0., 0., 1.]])
    if squeeze_axis == 'AXIS3_Z':
        return np.array([[1., 0., 0.], [0., 1., 0.]])


def projection_2to3(append_axis):
    if not append_axis in ('AXIS3_X', 'AXIS3_Y', 'AXIS3_Z'):
        raise ValueError("Unsupported squeeze axis {}.".format(append_axis))
    if append_axis == 'AXIS3_X':
        return np.array([[0., 0.], [1., 0.], [0., 1.]])
    if append_axis == 'AXIS3_Y':
        return np.array([[1., 0.], [0., 0.], [0., 1.]])
    if append_axis == 'AXIS3_Z':
        return np.array([[1., 0.], [0., 1.], [0., 0.]])
