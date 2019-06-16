import numpy as np


class Graph:
    """Class that specifies graph.

    Graph is an object that consists of vertices and edges.
    We can divide it into several objects, each object contains as many vertices
    as the number of letters in alphabet.
    We assign label to each vertex, in out case letters.
    For each vertex and edge we can assign a weight.
    We represent graph as a matrix of vertex weights and 4-dimensional array for edge weights.
    """

    def __init__(self, alphabet, string):
        self.alphabet = alphabet
        self.string = string
        self.objects_number = string.shape[1]
        self.vertex_weights = np.zeros((self.objects_number, len(alphabet)))
        self.edge_weights = np.inf * np.ones((self.objects_number, self.objects_number,
                                              len(alphabet), len(alphabet)))

        self.mapping = {i: char for i, char in enumerate(self.alphabet)}

    def init_edges(self):
        for i in np.arange(self.objects_number)[::-1]:
            for char in self.mapping:
                char_image = self.alphabet[self.mapping[char]]
                char_width = char_image.shape[1]
                if i - char_width + 1 < 0:
                    continue

                self.edge_weights[i - char_width, i, :, char] = np.sum((char_image
                                                                        - self.string[:, i - char_width + 1:i + 1])**2)

