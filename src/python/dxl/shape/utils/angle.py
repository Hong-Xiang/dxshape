from .vector import Vector2, Vector3, VectorLowDim
from abc import ABCMeta, abstractmethod, abstractclassmethod
import math
from typing import Tuple

__all__ = ['Angle', 'SolidAngle']


def theta2vector2(theta: float) -> Vector2:
    if theta is None:
        return None
    return Vector2([math.sin(theta), math.cos(theta)])


def vector22theta(v: Vector2) -> float:
    if v is None:
        return None
    return math.atan2(v.y(), v.x())


def theta_phi2vector3(theta: float, phi: float) -> Vector3:
    return Vector3([math.sin(theta) * math.sin(phi),
                    math.sin(theta) * math.cos(phi),
                    math.cos(theta)])


def vector32theta_phi(v: Vector3)-> Tuple[float, float]:
    if v is None:
        return None, None
    return math.acos(v.z()), math.atan2(v.y(), v.x())


class AngleBase(metaclass=ABCMeta):
    @abstractmethod
    def direction_vector(self) -> VectorLowDim:
        pass

    @abstractmethod
    def from_direction_vector(self, direction_vector) -> 'AngleBase':
        pass


class Angle(AngleBase):
    def __init__(self, theta=None):
        if theta is None:
            theta = 0.0
        self._theta = theta

    def theta(self):
        return self._theta

    def direction_vector(self) -> Vector2:
        return theta2vector2(self.theta())

    @classmethod
    def from_direction_vector(cls, v: Vector2) -> 'Angle':
        return cls(vector22theta(v))


class SolidAngle(AngleBase):
    def __init__(self, theta=None, phi=None):
        if theta is None:
            theta = 0.0
        if phi is None:
            phi = 0.0
        self._theta = theta
        self._phi = phi

    def theta(self):
        return self._theta

    def phi(self):
        return self._phi

    def direction_vector(self) -> Vector3:
        return theta_phi2vector3(self.theta(), self.phi())

    @classmethod
    def from_direction_vector(self, v: Vector3):
        return SolidAngle(*vector32theta_phi(v))


class AngleRangeBase(metaclass=ABCMeta):
    _vertex_cls = None

    @classmethod
    def _process_none_inputs(cls, start: AngleBase, end: AngleBase=None):
        if end is None:
            return cls._vertex_cls, start
        else:
            return start, end

    def __init__(self, start: AngleBase, end: AngleBase=None):
        self._start, self._end = self._process_none_inputs(start, end)

    def start(self) -> AngleBase:
        return self._start

    def end(self) -> AngleBase:
        return self._end

    @abstractmethod
    def start_unit_vector(self) -> VectorLowDim:
        pass

    @abstractmethod
    def end_unit_vector(self) -> VectorLowDim:
        pass

    @abstractmethod
    def from_direction_vectors(self, direction_vector, end_vector=None) -> 'AngleRangeBase':
        pass


class AngleRange(AngleRangeBase):
    _vertex_cls = Angle

    def __init__(self, theta0: Angle, theta1: Angle=None):
        self._start = Angle(theta0)
        self._end = Angle(theta1)

    def theta0(self):
        return self.start().theta()

    def theta1(self):
        return self.end().theta()

    @classmethod
    def from_direction_vectors(cls, start, end=None) -> SolidAngle:
        return cls(Angle.from_direction_vector(start),
                   Angle.from_direction_vector(end))

    def start_unit_vector(self) -> Vector2:
        return self.start().to_unit_vector()

    def end_unit_vector(self) -> Vector2:
        return self.end().to_unit_vector()


class SolidAngleRange(AngleRangeBase):
    def __init__(self, theta0, phi0, theta1=None, phi1=None):
        super().__init__(theta0, theta1)
        self._phi0, self._phi1 = self._process_none_inputs(phi0, phi1)

    def theta0(self):
        return self.start().theta()

    def theta1(self):
        return self.end().theta()

    def phi0(self):
        return self.start().phi()

    def phi1(self):
        return self.end().phi()

    def start_unit_vector(self) -> Vector3:
        return self.start().direction_vector()

    def end_unit_vector(self) -> Vector3:
        return self.end().direction_vector()

    @classmethod
    def from_direction_vector(cls, start, end=None) -> SolidAngle:
        return cls(SolidAngle(start), SolidAngle(end))
