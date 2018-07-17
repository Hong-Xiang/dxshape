import numpy as np


class Vector(np.ndarray):
    def __new__(cls, data):
        return np.reshape(np.squeeze(np.asarray(data)), [-1, 1]).view(cls)
