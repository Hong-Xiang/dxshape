from .base import Entity
from doufo import List, Functor, concat
from doufo.tensor import Vector

__all__ = ['Group', 'CartesianRepeater', 'RingRepeater']


class Group(Functor[Entity]):
    def __init__(self, es):
        self.es = List(es)

    def unbox(self):
        return self.es

    def fmap(self, f):
        return Group(self.es.fmap(f))

    def translate(self, v):
        return self.fmap(lambda e: e.translate(v))

    def rotate(self, axis, theta):
        return self.fmap(lambda e: e.rotate(axis, theta))

    def flatten(self):
        return concat(self.es.fmap(flatten_kernel), None)

    def __repr__(self):
        return f"<Group({self.es})>"


class CartesianRepeater(Group):
    def __init__(self, prototype, steps, grids):
        #default normal vector is axis-z
        from dxl.shape.function.group import moves, offsets
        f_shape = Vector([s*g for s, g in zip(steps, grids)])
        super().__init__((moves(offsets(steps, grids))
                          .fmap(lambda v: prototype.translate(v + Vector(steps)/2 - f_shape/2))))
        self.prototype = prototype
        self.steps = steps
        self.grids = grids

class RingRepeater(Group):
    def __init__(self, prototype, steps, num, axis):
        from dxl.shape.function.group import offsets
        import numpy as np
        super().__init__(List(np.array(offsets([steps], [num])).flatten())
                         .fmap(lambda v: prototype.rotate(axis, v)))
        self.prototype = prototype
        self.steps = steps
        self.num = num

def flatten_kernel(e):
    if isinstance(e, Entity):
        return List([e])
    if isinstance(e, Group):
        return e.flatten()
    raise TypeError(f"{type(e)} not supported for flatten.")
