import random as rd
import math
def random_points(radius, x_center, y_center):
    r = math.sqrt((radius**2) * rd.random())
    theta = 2 * math.pi * rd.random()        
    return [x_center + r * math.cos(theta), y_center + r * math.sin(theta)]
