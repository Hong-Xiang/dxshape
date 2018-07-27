from .base import Entity
from dxl.data import List


class Group:
    def __init__(self, es):
        self.es = List(es)

    def fmap(self, f):
        return Group(self.es.fmap(f))

    def flatten(self):
        return self.es.fmap(flatten_kernel)


def flatten_kernel(e):
    if isinstance(e, Entity):
        return List([e])
    if isinstance(e, Group):
        return e.flatten()
    raise TypeError(f"{type(e)} not supported for flatten.")
