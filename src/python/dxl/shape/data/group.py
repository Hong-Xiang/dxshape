from .base import Entity
from dxl.data import List
from dxl.function import concat

__all__ = ['Group']


class Group:
    def __init__(self, es):
        self.es = List(es)

    def fmap(self, f):
        return Group(self.es.fmap(f))

    def translate(self, v):
        return self.fmap(lambda e: e.translate(v))

    def rotate(self, axis, theta):
        return self.fmap(lambda e: e.rotate(axis, theta))

    def flatten(self):
        return concat(self.es.fmap(flatten_kernel))

    def __repr__(self):
        return f"<Group({self.es})>"


def flatten_kernel(e):
    if isinstance(e, Entity):
        return List([e])
    if isinstance(e, Group):
        return e.flatten()
    raise TypeError(f"{type(e)} not supported for flatten.")
