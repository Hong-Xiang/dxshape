from .base import Entity
from dxl.data import List, Functor
from dxl.data.tensor import Vector
from dxl.function import concat

__all__ = ['Group', 'CartesianRepeated']


class Group(Functor[Entity]):
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


class CartesianRepeated(Group):
    def __init__(self, prototype, steps, grids):
        from dxl.shape.function.group import moves, offsets
        f_shape = Vector([s*g for s, g in zip(steps, grids)])
        super().__init__((moves(offsets(steps, grids))
                          .fmap(lambda v: prototype.translate(v + steps / 2- f_shape/2))))


def flatten_kernel(e):
    if isinstance(e, Entity):
        return List([e])
    if isinstance(e, Group):
        return e.flatten()
    raise TypeError(f"{type(e)} not supported for flatten.")
