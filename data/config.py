import random
import math

width = 600
height = 600
grid_size = 20


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    dist = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    return dist


def rand_location():
    rows = height // grid_size
    cols = width // grid_size
    x = random.randint(0, rows-1) * grid_size
    y = random.randint(0, cols-1) * grid_size
    return (x, y)
