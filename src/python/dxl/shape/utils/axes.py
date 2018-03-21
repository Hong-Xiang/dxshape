from .vector import Vector3


class Axis3:
    def __init__(self, direction_vector: Vector3):
        self._v = direction_vector

    def direction_vector(self):
        return self._v


AXIS3_X = Axis3(Vector3([1.0, 0.0, 0.0]))
AXIS3_Y = Axis3(Vector3([0.0, 1.0, 0.0]))
AXIS3_Z = Axis3(Vector3([0.0, 0.0, 1.0]))


class Axes3:
    def __init__(self, x_axis, y_axis, z_axis):
        self._x = x_axis
        self._y = y_axis
        self._z = z_axis


AXES3_STD = Axes3(AXIS3_X, AXIS3_Y, AXIS3_Z)
