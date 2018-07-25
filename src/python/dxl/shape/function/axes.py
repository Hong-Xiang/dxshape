from dxl.shape.data import Vector, AXES3
from .op_matrix import axis_to_axis
from dxl.function.tensor import norm


def axis_x_of(n: Vector) -> Vector:
    """
    Returns:
        x axis if z is n.
    """
    # FIXME add support for AXIS
    result = axis_to_axis(n, AXES3.z.normal) @ AXES3.x
    return result / norm(result)


def axis_y_of(n: Vector) -> Vector:
    result = axis_to_axis(n, AXES3.z.normal) @ AXES3.y
    return result / norm(result)
