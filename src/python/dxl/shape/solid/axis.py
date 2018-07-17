from .base import Entity
import numpy as np
from abc import ABCMeta


class Axis(Entity):
    def __init__(self, normal, origin=None):
        super().__init__(origin, normal)

    def replace(self, origin=None, normal=None):
        return Axis(**self._replace_dict(origin, normal))
   
    def _rotate_on_direction(self, direction, theta):
        pass

