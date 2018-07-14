from .base import Shape
from .point import Point
from .box import Box
from ..rotation.matrix import axis_to_axis
from ..utils.vector import Vector3
import numpy as np


class CollisionTesterManager:
    @classmethod
    def get(s0: Shape, s1: Shape):
        pass


#class CollisionTester:
#    def is_collision( s0: Shape, s1: Shape) -> bool:
#       pass


#class BoxPointTester:
#    def __init__(self, p: Point, b: Box):
#        if isinstance(p, Box):
#            p, b = b, p
#        self._point = p
#        self._box = b

def is_collision(p: Point, b: Box) -> bool:
    if isinstance(p, Box):
        p, b = b, p
    boolValue=False
    bTrans=b.translate( b.origin*[-1])
    pTtans=p.translate( b.origin*[-1])
    RotateMatrix=axis_to_axis(b.normal,[0.0, 0.0, 1.0])
    pRot=np.dot(RotateMatrix, pTtans)
    if ((pRot[1]<=0.5*bTrans. shape[1] or pRot[1]>=-0.5*bTrans. shape[1]) and 
        (pRot[2]<=0.5*bTrans. shape[2] or pRot[2]>=-0.5*bTrans. shape[2]) and
        (pRot[3]<=0.5*bTrans. shape[3] or pRot[3]>=-0.5*bTrans. shape[3])):
        boolValue=not boolValue
    return boolValue