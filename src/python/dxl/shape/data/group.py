from .base import Entity
from dxl.data import List, Functor
from dxl.data.tensor import Vector
from dxl.function import concat

__all__ = ['Group', 'CartesianRepeated', 'LinearRepeated']


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
        #default normal vector is axis-z
        from dxl.shape.function.group import moves, offsets
        f_shape = Vector([s*g for s, g in zip(steps, grids)])
        super().__init__((moves(offsets(steps, grids))
                          .fmap(lambda v: prototype.translate(v + steps / 2 - f_shape/2))))

class LinearRepeated(Group):
    def __init__(self, prototype, steps, num: List[int]):
        from dxl.shape.function.group import moves, offsets
        f_shape = Vector([s*g for s, g in zip(steps, num)])
        super().__init__((moves(offsets(steps, num))
                           .fmap(lambda v: prototype.translate(v + steps / 2 - f_shape/2))))

# class RingRepeated(Group):
#     def __init__(self, prototype, )


def flatten_kernel(e):
    if isinstance(e, Entity):
        return List([e])
    if isinstance(e, Group):
        return e.flatten()
    raise TypeError(f"{type(e)} not supported for flatten.")
