from math import log
from collections import namedtuple
from generate import generate_image

Pixel = namedtuple("Pixel", "i j")

class ImageGraph:
    def __init__(self, image, eps=0.1, beta=0.7):
        self.image = image
        self.eps = eps
        self.beta = beta

    def pixel_cost(self, pixel, label):
        return -log(self.eps) if self.image[pixel.i, pixel.j] != label else -log(1 - self.eps)

    def edge_cost(self, pixel1, pixel2):
        if self.image[pixel1.i, pixel1.j] != self.image[pixel2.i, pixel2.j]:
            return self.beta
        else:
            return 0

    def neighbours(self, pixel):
        i, j = pixel
        if i == 0:
            if j == 0:
                neighbours_list = [Pixel(i+1, j), (i, j + 1)] 
            elif j == self.image.shape[1] - 1:
                neighbours_list = [Pixel(i, j-1), Pixel(i + 1, j)] 
            else:
                neighbours_list = [Pixel(i, j - 1), Pixel(i+1, j), Pixel(i, j + 1)]
        elif i == self.image.shape[0] - 1:
            if j == 0:
                neighbours_list = [Pixel(i - 1, j), Pixel(i, j + 1)]
            elif j == self.image.shape[1] - 1:
                neighbours_list = [Pixel(i - 1, j), Pixel(i, j - 1)]
            else:
                neighbours_list = [Pixel(i, j - 1), Pixel(i - 1, j), Pixel(i, j + 1)]
        else:
            neighbours_list = [Pixel(i - 1, j), Pixel(i, j - 1), Pixel(i + 1, j), Pixel(i, j + 1)]

        return neighbours_list

    