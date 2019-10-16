from math import log
from collections import namedtuple
import numpy as np

Pixel = namedtuple("Pixel", "i j label")

def pixel_cost(pixel, label, eps=0.1):
    return -log(eps) if pixel.label != label else -log(1 - eps)

def edge_cost(pixel1, pixel2, beta=0.7):
    if pixel1.label != pixel2.label:
        return beta
    else:
        return 0

def neighbours(image, i, j):
    padding = (-1) * np.ones(
        (image.shape[0] + 2, 
         image.shape[1] + 2)
    )
    padding[1:-1, 1:-1] = image
    neighbours = [Pixel(i + 1, j, padding[i + 1, j]), 
                    Pixel(i, j + 1, padding[i, j + 1]),
                    Pixel(i + 1, j + 2, padding[i + 1, j + 2]),
                    Pixel(i + 2, j + 1, padding[i + 2, j + 1])]

    neighbours = list(filter(lambda x: x.label != -1, neighbours))
    neighbours = [Pixel(x.i - 1, x.j - 1, x.label) for x in neighbours]
    return neighbours
