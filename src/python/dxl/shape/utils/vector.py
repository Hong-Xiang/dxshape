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
        if np.array(v).size == 3:
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
        self._data = np.array(data).reshape([self.dim(), 1])
        if self.dim() is not None and self.data().size != self.dim():
            fmt = "Invalid data dimension {} when {} is expected for {}."
            raise ValueError(
                fmt.format(self.data().size, self.dim(), __class__))

    @classmethod
    def zeros(cls):
        return cls(np.zeros([cls.dim()]))

    def __getattr__(self, key):
        return getattr(self._data, key)

    def __add__(self, v: 'VectorLowDim'):
        if isinstance(v, VectorLowDim):
            data = v.data()
        return self.__class__(self.data() + data)

    def __radd(self, v):
        return self.__add__(v)

    def __sub__(self, v: 'VectorLowDim'):
        return self.__class__(self.data() - v.data())

    def __eq__(self, v):
        if isinstance(v, VectorLowDim):
            raw_data = v._data
        else:
            raw_data = np.array(v)
        return np.array_equal(self._data, raw_data)

    def to_direction_vector(self):
        return self.__class__(self.data() / np.linalg.norm(self.data()))

    def __getitem__(self, i):
        return self._data[i]


class Vector1(VectorLowDim):
    def x(self):
        return self.data()[0]

    @classmethod
    def dim(self):
        return 1


class Vector2(VectorLowDim):
    def x(self):
        return self.data()[0]

    def y(self):
        return self.data()[1]

    @classmethod
    def dim(self):
        return 2


class Vector3(VectorLowDim):
    @classmethod
    def dim(self):
        return 3

    def x(self):
        return self.data()[0]

    def y(self):
        return self.data()[1]

    def z(self):
        return self.data()[2]

    def __sub__(self, v):
        return Vector3(self.data() - v.data())

    def norm(self):
        return np.linalg.norm(self.data())

    def __repr__(self):
        return "<Vector3([{}, {}, {}])>".format(self.x(), self.y(), self.z())