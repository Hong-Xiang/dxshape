"""
This file define the Quaternion class for 3D rotation.
"""

from doufo import dataclass
import numpy as np

__all__ = ['Quaternion', 'make_rotate_matrix']


@dataclass
class Quaternion():
    w: float
    x: float
    y: float
    z: float


def make_rotate_matrix(qua: Quaternion) ->np.array:
    [w, x, y, z] = [qua.w, qua.x, qua.y, qua.z]
    [x, y, z] = [x, y, z]/np.linalg.norm(np.array([x, y, z]))
    q0 = np.cos(w/2)
    q1 = np.sin(w/2)*x
    q2 = np.sin(w/2)*y
    q3 = np.sin(w/2)*z
    return np.array([[q0**2 + q1**2 - q2**2 - q3**2, 2*(q1*q2 - q0*q3), 2*(q1*q3 + q0*q2)],
                     [2*(q1*q2 + q0*q3), q0**2 - q1**2 +
                         q2**2 - q3**2, 2*(q2*q3 - q0*q1)],
                     [2*(q1*q3 - q0*q2), 2*(q2*q3 + q0*q1), q0**2 - q1**2 - q2**2 + q3**2]])
