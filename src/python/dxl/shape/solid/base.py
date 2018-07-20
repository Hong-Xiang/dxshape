#from ..utils import AngleBase
#from .axis import Axis 
from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

class NamedTuple:
    def replace(self, **kwargs):
        for k in self.__slot__:
            if not k in kwargs:
                kwargs[k] = getattr(self, k)                
        return type(self)(**kwargs)
    # def _replace(_self, **kwds):
    #     'Return a new {typename} object replacing specified fields with new values'
    #     result = _self._make(map(kwds.pop, {field_names!r}, _self))
    #     if kwds:
    #         raise ValueError('Got unexpected field names: %r' % list(kwds))
    #     return result

    def __repr__(self): 
        class_name = type(self).__name__  
        inner = {k: getattr(self, k) for k in self.__slot__} 
        return f"{class_name}({inner})"  
        #inner = json.dumps({k: getattr(self, k) for k in self.__slot__}, separators=(',', ':'))
        #return f"<{type(self)}({inner})>"
    
    def __eq__(self, others) -> bool: 
        result = True
        result = ((result and (getattr(self, k)==getattr(others, k))) for k in self.__slot__)          
        return result

    # this is '__eq__' in Vector.py
    #  def __eq__(self, v):
    #     if isinstance(v, VectorLowDim):
    #         raw_data = v._data
    #     else:
    #         raw_data = np.array(v)
    #     return np.array._equal(self._data, raw_data)

class Entity(NamedTuple):

    @property
    def ndim(self):
        return len(self.origin)

    def translate(self, v):
        return self.replace(origin = self.origin + v)

    @abstractmethod
    def _rotate_on_direction(self, direction, theta):
        pass

    def rotate(self, axis, theta: float):
        if np.allclose(axis.origin, 0.0):
            return self._rotate_on_direction(axis.direction, theta)
        return (self.translate(-axis.origin)
                ._rotate_on_direction(axis.normal, theta)
                .translate(axis.origin))

class LinearSpace:
    @property
    def ndim(self):
        pass

class R3(LinearSpace):
    @property
    def ndim(self):
        return 3



