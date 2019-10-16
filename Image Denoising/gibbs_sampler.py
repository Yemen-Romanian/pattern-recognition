from graph import (
    Pixel,
    pixel_cost,
    edge_cost,
    neighbours
)
import numpy as np

def sample_pixel(i, j, image, labels):
    probs = []
    for label in labels:
        pixel = Pixel(i, j, label)
        pxl_cost = pixel_cost(pixel, label)
        neighbour_pxls = neighbours(image, pixel)
        neighbours_costs = []
        for neighbour in neighbour_pxls:
            neighbours_costs += [edge_cost(pixel, neighbour)]

        probs.append(np.exp(-pxl_cost - np.sum(neighbours_costs)))

    probs = probs / np.sum(probs)
    sampled_pixel = np.random.choice(labels, p=probs)
    return sampled_pixel


def step(image, labels):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j] = sample_pixel(i, j, image, labels)

    return image



        

            