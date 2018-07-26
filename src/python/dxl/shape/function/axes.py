from dxl.shape.data import Vector, AXES3
from dxl.function.tensor import norm


def axis_x_of(n: Vector) -> Vector:
    """
    Returns:
        x axis if z is n.
    """
    # FIXME add support for AXIS
    result = Vector([n.y, -n.x, 0.0])
    return result / norm(result)


def axis_y_of(n: Vector) -> Vector:
    x = axis_x_of(n)
    result = outer_product(n, x)
    return result / norm(result)


def outer_product(a: Vector, b: Vector):
    return Vector([a.y * b.z - a.z * b.y,
                   a.z * b.x - a.x * b.z,
                   a.x * b.y - a.y * b.x])
