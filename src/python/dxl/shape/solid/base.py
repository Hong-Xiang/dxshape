#from ..utils import AngleBase
#from .axis import Axis 
from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np
#from collections import namedtuple

class NamedTuple:
    def replace(self, **kwargs):
        for k in self.__slot__:
            if not k in kwargs:
                kwargs[k] = getattr(self, k)                
        return type(self)(**kwargs)

    def __repr__(self): 
        class_name = type(self).__name__  
        inner = {k: getattr(self, k) for k in self.__slot__} 
        return f"{class_name}({inner})"  
    
    def __eq__(self, others) -> bool:              
        return all(getattr(self, k)== getattr(others, k) for k in self.__slot__)
            
class Entity(NamedTuple):
    @property
    def ndim(self):
        return len(self.origin)

    def translate(self, v: np.ndarray):
        return self.replace(origin = np.array(self.origin) + v)

    @abstractmethod
    def _rotate_on_direction(self, direction, theta):
        pass

    def rotate(self, axis: 'Axis', theta: float):
        from dxl.shape.solid.axis import Axis
        if np.allclose(axis.origin, 0.0):
            return self._rotate_on_direction(axis.direction_vector, theta)
        return (self.translate(-axis.origin)
                ._rotate_on_direction(axis.direction_vector, theta)
                .translate(axis.origin))



class LinearSpace:
    @property
    def ndim(self):
        pass

class R3(LinearSpace):
    @property
    def ndim(self):
        return 3



