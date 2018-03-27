import numpy as np


class VectorLowDim:
    _dim = None

    def data(self):
        return self._data

    @classmethod
    def from_list(cls, v):
        if np.array(v).size == 1:
            return Vector1(v)
        if np.array(v).size == 2:
            return Vector2(v)
        if np.array(v) == 3:
            return Vector3(v)

    @classmethod
    def dim(cls):
        return cls._dim

    def __init__(self, data):
        """
        Parameters:

        - `data`: VectorLowDim, list/tuple or numpy.ndarray of correspongding dimension.

        Raises:

        - `TypeError` if given data with unsupported type.
        - `ValueError` if given data with invalid dimension.
        """
        self._data = np.array(data).reshape([self.dim()])
        if self.dim() is not None and self.data().size != self.dim():
            fmt = "Invalid data dimension {} when {} is expected for {}."
            raise ValueError(fmt.format(self.data().size,
                                        self.dim(), __class__))

    @classmethod
    def zeros(cls):
        return cls(np.zeros([cls.dim()]))

    def __add__(self, v: 'VectorLowDim'):
        return self.data() + v.data()

    def __reduce__(self, v: 'VectorLowDim'):
        return self.data() - v.data()


class Vector1(VectorLowDim):
    _dim = 1

    def x(self):
        return self.data()[0]


class Vector2(VectorLowDim):
    _dim = 2

    def x(self):
        return self.data()[0]

    def y(self):
        return self.data()[1]


class Vector3(VectorLowDim):
    _dim = 3

    def x(self):
        return self.data()[0]

    def y(self):
        return self.data()[1]

    def z(self):
        return self.data()[2]
