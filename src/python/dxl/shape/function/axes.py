from dxl.shape.data import Vector, AXES3
from dxl.function.tensor import norm, argmax, abs_, unit


def axis_x_of(n: Vector) -> Vector:
    """
    Returns:
        x axis if z is n.
    """
    # FIXME add support for AXIS, lazy vector
    n = unit(Vector(n))
    main_index_of_n = argmax(abs_(n))
    result = [0.0, 0.0, 0.0]
    main_index_of_result = (main_index_of_n + 1) % 3
    result[main_index_of_result] = n[main_index_of_n]
    result[main_index_of_n] = -n[main_index_of_result]
    return unit(Vector(result))


def axis_y_of(n: Vector) -> Vector:
    n = unit(Vector(n))
    return unit(outer_product(n, axis_x_of(n)))


def outer_product(a: Vector, b: Vector):
    return Vector([a.y * b.z - a.z * b.y,
                   a.z * b.x - a.x * b.z,
                   a.x * b.y - a.y * b.x])
