import cv2
import maxflow
import numpy as np
import matplotlib.pyplot as plt
from graph import(
    pixel_cost,
    edge_cost,
    neighbours,
    Pixel
)

from noise import salt_and_pepper_noise


def create_graph(labeling, alpha, L, S):
    graph = maxflow.Graph[float]()
    height, width = labeling.shape
    nodeids = graph.add_grid_nodes(labeling.shape)

    for i in range(height):
        for j in range(width):
            current_pxl = Pixel(i, j, labeling[i, j])
            current_label = current_pxl.label
            neighbours_list = neighbours(labeling, i, j)
            for neighbour in neighbours_list:
                weight = edge_cost(current_pxl, neighbour, S, L)
                graph.add_edge(nodeids[i, j], nodeids[neighbour.i, neighbour.j], weight, weight)

            pxl_weight_0 = pixel_cost(current_pxl, current_label)
            pxl_weight_1 = pixel_cost(current_pxl, alpha)
            graph.add_tedge(nodeids[i, j], pxl_weight_0, pxl_weight_1)

    return graph, nodeids


def maxflow_denoising(image, S=10, L=10):
    graph, nodeids = create_graph(image, L, S)
    graph.maxflow()
    sgm = graph.get_grid_segments(nodeids)
    result = (np.logical_not(sgm)).astype(int)
    plt.imshow(result, cmap='gray')
    plt.savefig('Result.png')

if __name__ == '__main__':
    image = cv2.imread('examples/barbara.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (100, 100))
    plt.imshow(image, cmap='gray')
    plt.show()
    noised = salt_and_pepper_noise(image)
    plt.imshow(noised, cmap='gray')
    plt.show()
    K = np.arange(0, 256)
    np.random.shuffle(K)
    labeling = noised
    L, S = 20, 10
    i = 1
    for alpha in K:
        print(i)
        graph, nodeids = create_graph(labeling, alpha, L, S)
        graph.maxflow()
        segments = graph.get_grid_segments(nodeids)
        labeling[np.logical_not(segments)] = alpha
        i += 1

    plt.imshow(labeling, cmap='gray')
    plt.show()


