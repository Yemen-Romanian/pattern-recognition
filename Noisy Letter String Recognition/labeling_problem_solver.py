import numpy as np


class LPSolver:
    """Class for solving labeling problem on given graph."""

    def __init__(self, graph):
        self.graph = graph
        self.labels = np.zeros(self.graph.vertex_weights.shape)

    def solve(self):
        """Returns graph labeling (in our case sequence of letters) that minimizes
        the path weight, and the minimum path weight itself."""
        for i in np.arange(1, self.graph.objects_number):
            for char in self.graph.mapping:
                char_width = self.graph.alphabet[self.graph.mapping[char]].shape[1]
                path_weights = self.graph.vertex_weights[i - char_width, :] + \
                               self.graph.edge_weights[i - char_width, i, :, char]

                self.graph.vertex_weights[i, char] = np.min(path_weights)

                self.labels[i, char] = np.argmin(path_weights)

        result = ''
        i = self.graph.objects_number - 1
        while i > 0:
            label = np.argmin(self.graph.vertex_weights[i, :])
            result = self.graph.mapping[label] + result
            i = i - self.graph.alphabet[self.graph.mapping[label]].shape[1]

        min_path_weight = np.min(self.graph.vertex_weights[-1, :])
        print('Minimum path weight: {}'.format(min_path_weight))
        print('Recognized string: {}'.format(result))
        return result, min_path_weight

