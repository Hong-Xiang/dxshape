from .vector import Vector2, Vector3, VectorLowDim
from abc import ABCMeta, abstractmethod
import math
from typing import Tuple


class AngleBase(metaclass=ABCMeta):
    @abstractmethod
    @classmethod
    def _process_angle_base(cls, angle):
        pass

    @abstractmethod
    def unit_vector(self) -> VectorLowDim:
        pass

    @abstractmethod
    def from_unit_vector(cls, unit_vector) -> 'AngleBase':
        pass


class AngleRangeBase(metaclass=ABCMeta):
    _vertex_cls = None

    @classmethod
    def _process_none_inputs(cls, start: AngleBase, end: AngleBase=None):
        if end is None:
            return cls._vertex_cls(), start
        else:
            return start, end

    def __init__(self, start: AngleBase, end: AngleBase=None):
        self._start, self._end = self._process_none_inputs(start, end)

    def start(self) -> AngleBase:
        return _start

    def end(self) -> AngleBase:
        return _end

    @abstractmethod
    def start_unit_vector(self) -> VectorLowDim:
        pass

    @abstractmethod
    def end_unit_vector(self) -> VectorLowDim:
        pass

    @abstractmethod
    def from_unit_vector(cls, unit_vector, end_vector=None) -> 'AngleRangeBase':
        pass


def theta2vector2(theta: float) -> Vector2:
    if theta is None:
        return None
    return Vector2([math.sin(theta), math.cos(theta)])


def vector22theta(v: Vector2) -> float:
    if v is None:
        return None
    return math.atan2(v.y(), v.x())


class Angle(AngleBase):
    def __init__(self, theta=None):
        if theta is None:
            theta = 0.0
        self._theta = theta

    def theta(self):
        return self._theta

    def unit_vector(self) -> Vector2:
        return theta2vector2(self.theta())

    @classmethod
    def from_unit_vector(cls, v: Vector2) -> 'Angle':
        return cls(vector22theta(v))


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
    def from_unit_vector(cls, start, end=None) -> SolidAngle:
        return cls(Angle.from_unit_vector(start),
                   Angle.from_unit_vector(end))

    def start_unit_vector(self) -> Vector2:
        return self.start().to_unit_vector()

    def end_unit_vector(self) -> Vector2:
        return self.end().to_unit_vector()


def theta_phi2vector3(theta: float, phi: float) -> Vector3:
    return Vector3([math.cos(theta) * math.sin(phi),
                    math.cos(theta) * math.cos(phi),
                    math.sin(theta)])


def vector32theta_phi(v: Vector3)-> Tuple[float, float]:
    if v is None:
        return None, None
    return math.asin(v.z()), math.atan2(v.y(), v.x())


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

    def unit_vector(self):
        return theta_phi2vector3(self.theta(), self.phi())


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
        return self.start().unit_vector()

    def end_unit_vector(self) -> Vector3:
        return self.end().unit_vector()

    @classmethod
    def from_unit_vector(cls, start, end=None) -> SolidAngle:
        return cls(SolidAngle(start), SolidAngle(end))
