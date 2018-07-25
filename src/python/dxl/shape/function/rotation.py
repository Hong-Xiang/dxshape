from functools import singledispatch
from dxl.shape.data import Entity, Vector, Axis, AXES3
from .op_matrix import axis_to_z, rotate2, rotate3, z_to_axis


@singledispatch
def rotate(o, axis_like, theta):
    raise TypeError(f"{type(o)} not support for rotate.")

# FIXME duplicate axis_like check and raise error


@rotate.register(Vector)
def _(v, axis_like, theta):
    return rotate_vector(v, Axis(axis_like), theta)


def rotate_vector(v, a, theta):
    return axis_to_z(a) @ rotate_of_dim(theta, v.ndim) @ z_to_axis(a) @ v


def rotate_of_dim(theta, dim):
    if dim == 2:
        return rotate2(theta)
    else:
        return rotate3(theta, AXES3.z)


@rotate.register(Entity)
def _(o, axis_like, theta):
    return o.rotate(Axis(axis_like), theta)
