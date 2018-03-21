import numpy as np
from ..utils.axes import Axes3, Axis3

def radians3x(r:float, axis: Axis3):
    

def axes2z(axes):
    """
    rotation matrix rotate z axis of given axes to normal z axis
    """
    pass


def z2axes(axes):
    """
    rotation matrix which rotate normal z axis to z axis of given axes
    """


def axes2axes(source, target):
    """
    rotation matrix which rotate z axis of source axes to z axis of target axes
    """
    return axes2z(source) @ z2axes(target)
