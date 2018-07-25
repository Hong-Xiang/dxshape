from .base import Existence
from abc import abstractmethod
import collections.abc


class Region(Existence, collections.abc.Container):
    @abstractmethod
    def __contains__(self, e) -> bool:
        pass


class WholeSpace(Region):
    def __contains__(self, e) -> bool:
        return e.ndim == self.ndim


class R3(Region):
    @property
    def ndim(self):
        return 3
