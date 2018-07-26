from dxl.shape.data import Vector, AXES3
from dxl.function.tensor import norm, argmax


def axis_x_of(n: Vector) -> Vector:
    """
    Returns:
        x axis if z is n.
    """
    # FIXME add support for AXIS
    n = Vector(n)
    m = argmax(n)
    result = [0.0, 0.0, 0.0]
    result[m] = n[m]
    result[(m + 1) % 3] = - n[(m + 1) % 3]
    result = Vector(result)
    return result / norm(result)


def axis_y_of(n: Vector) -> Vector:
    n = Vector(n)
    x = axis_x_of(n)
    result = outer_product(n, x)
    return result / norm(result)


def outer_product(a: Vector, b: Vector):
    return Vector([a.y * b.z - a.z * b.y,
                   a.z * b.x - a.x * b.z,
                   a.x * b.y - a.y * b.x])
