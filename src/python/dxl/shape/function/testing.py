from dxl.shape.data import Entity, Point, Box
from functools import singledispatch
import dxl.function.tensor as dft


@singledispatch
def all_close(e0: Entity, e1: Entity):
    raise TypeError()


@all_close.register(Point)
def _(p0, p1):
    if not isinstance(p1, Point):
        raise TypeError()
    return dft.all_close(p0.origin, p1.origin)


@all_close.register(Box)
def _(b0, b1):
    if not isinstance(b1, Box):
        raise TypeError()
    return (dft.all_close(b0.origin, b1.origin)
            and dft.all_close(b0.normal,  b1.normal)
            and dft.all_close(b0.shape, b1.shape))
