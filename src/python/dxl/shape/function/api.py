from doufo import multidispatch, singledispatch
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def translate(e, r):
    pass


@multidispatch(nargs=2, nouts=1)
def rotate_by_matrix(e, m):
    raise NotImplementedError(f"No implementation for {type(e)}.")


from dxl.shape.data import Box, Point, Segment


@rotate_by_matrix.register(Box, np.ndarray)
@rotate_by_matrix.register(Box, object)
def _(b, m):
    return Box(b.shape, m@b.origin, m@b.normal)


@rotate_by_matrix.register(Point, object)
def _(p, m):
    return Point(m@p.origin)


@singledispatch(nargs=1)
def visual(e, *args):
    raise NotImplementedError(f"No implementation for {type(e)}.")

@visual.register(Point)
def _(e, *args):
    if len(args) == 0:
        args = ['.']
    plt.gca().plot3D(*[[o] for o in e.origin], *args)


@visual.register(Segment)
def _(seg, *args):
    plt.gca().plot3D(*[[f, s] for f, s in zip(seg.fst.origin, seg.snd.origin)], *args)
    
