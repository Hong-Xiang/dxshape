import numpy as np
import math


class Line:
    def __init__(self, origin, normal):
        self.origin = origin
        self.normal = normal

    def distance_to(self, s):
        pass

def get_container_plane_in_R3(p0, normal_vector):
    return np.array(np.array(normal_vector).tolist() + [-np.sum(normal_vector)])

def distance_of_lines(line0, line1):
    pass
    
