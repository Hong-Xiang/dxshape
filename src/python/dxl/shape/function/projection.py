from dxl.shape.data import Vector, Matrix
from .axes import axis_x_of, axis_y_of
from dxl.function.tensor import all_close, project, argmax

# TODO enhance logic since lots of duplication

__all__ = ['project', 'embed']

def project(v: Vector, n: Vector):
    p = project(v, n)
    m = argmax(p)
    return Vector([x for i, x in enumerate(p) if i != m])


def embed(v: Vector, n: Vector):
    return Vector([axis_x_of(n) * v.x, axis_y_of(n) * v.y])

    

    # append_axis = Axis(append_axis)
    # if all_close(append_axis.normal, AXIS3_X.normal):
    #     return Matrix([[0., 0.], [1., 0.], [0., 1.]])
    # if all_close(append_axis.normal, AXIS3_Y.normal):
    #     return Matrix([[1., 0.], [0., 0.], [0., 1.]])
    # if all_close(append_axis.normal, AXIS3_Z.normal):
    #     return Matrix([[1., 0.], [0., 1.], [0., 0.]])
    # raise ValueError("Unsupported squeeze axis {}.".format(append_axis))
