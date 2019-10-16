from graph import (
    Pixel,
    pixel_cost,
    edge_cost,
    neighbours
)
import numpy as np

def sample_pixel(i, j, image, labels, eps, beta):
    """Sample pixel from conditional probability distribution.
    
    Arguments:
        i {int} -- row coordinate of pixel
        j {int} -- column coordinate of pixel
        image {numpy.ndarray} -- image
        labels {list} -- list of all labels ([0, 1] for black and white images)
        eps {float} -- noise parameter
        beta {float} -- edge cost parameter
    
    Returns:
        int -- sampled pixel
    """
    probs = []
    neighbour_pxls = neighbours(image, i, j)
    for label in labels:
        pixel = Pixel(i, j, label)
        pxl_cost = pixel_cost(pixel, image[i, j], eps)
        neighbours_costs = []
        for neighbour in neighbour_pxls:
            neighbours_costs += [edge_cost(pixel, neighbour, beta)]

        probs.append(np.exp(-pxl_cost - np.sum(neighbours_costs)))

    probs = probs / np.sum(probs)
    sampled_pixel = np.random.choice(labels, p=probs)
    return sampled_pixel


def step(image, labels, eps, beta):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j] = sample_pixel(i, j, image, labels, eps, beta)

    return image



        

            