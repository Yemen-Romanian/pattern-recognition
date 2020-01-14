import numpy as np
import matplotlib.pyplot as plt
from parse_tsukuba import load_downsampled_model
from grid import determine_grid
from tsukuba_visualize import to_image

LABELS_NUM = 16


def diffusion(grid, num_iters):
    edges_dict = {}

    for edge in grid._edges:
        edges_dict[(edge.left, edge.right)] = edge.costs
        edges_dict[(edge.right, edge.left)] = {(key[1], key[0]): value for key, value in edge.costs.items()}

    for iteration in range(num_iters):
        for n_node in range(len(grid._nodes)):
            node = grid._nodes[n_node]
            neighbours = grid.neighbors(n_node)
            number_of_neighbours = len(neighbours)
            for label in range(len(node.costs)):
                max_sum = 0
                for neighbour in neighbours:
                    costs = edges_dict[(n_node, neighbour)]
                    max_edge = max([costs[(label, label_)] for label_ in range(LABELS_NUM)])
                    max_sum += max_edge
                    node.costs[label] = (node.costs[label] + max_sum) / (number_of_neighbours + 1)
                    for label_ in range(LABELS_NUM):
                        max_edge = max([costs[(label, label_)] for label_ in range(LABELS_NUM)])
                        costs[(label, label_)] = costs[(label, label_)] + node.costs[label] - max_edge

        print(f'Iteration {iteration} completed')

    labeling = []
    for node in grid._nodes:
        labeling.append(np.argmin(node.costs))

    return labeling


def check_epsilon_consistency(grid, epsilon=0.1):
    pass

if __name__ == '__main__':
    nodes, edges = load_downsampled_model(4)
    grid = determine_grid(nodes, edges)
    print('Successfully loaded model')
    width, height = grid.width, grid.height
    labeling = diffusion(grid, 10)
    result = to_image(labeling, (height, width))
    plt.imshow(result, cmap='gray')
    plt.show()

