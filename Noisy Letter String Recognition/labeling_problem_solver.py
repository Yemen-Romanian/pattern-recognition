from graph import Graph
from generator import TTIGenerator
import numpy as np

class LPSolver:

    def __init__(self, graph):
        self.graph = graph
        self.labels = np.zeros(self.graph.vertix_weights.shape)

    def solve(self):
        for i in np.arange(1, self.graph.objects_number):
            for char in graph.mapping:
                char_width = self.graph.alphabet[self.graph.mapping[char]].shape[1]
                self.graph.vertix_weights[i, char] = np.min(self.graph.vertix_weights[i - char_width, :] +
                                                            self.graph.edge_weights[i - char_width, i, :, char])

                self.labels[i, char] = np.argmin(self.graph.vertix_weights[i - char_width, :] +
                                                            self.graph.edge_weights[i - char_width, i, :, char])

        result = ''
        i = self.graph.objects_number - 1
        while i > 0:
            label = np.argmin(self.graph.vertix_weights[i, :])
            result = self.graph.mapping[label] + result
            i = i - self.graph.alphabet[self.graph.mapping[label]].shape[1]
        print('Minimum path weight: ', np.min(self.graph.vertix_weights[-1, :]))
        print('Recognized string: ', result)



if __name__ == '__main__':
    generator = TTIGenerator('images')
    string = generator.add_noise(generator.text_to_image('AB___CC___BCAA_A'), sigma=0.9)
    #string = generator.text_to_image('AAAAAABC__CAB_C_A_B')
    graph = Graph(generator.alphabet, string)
    graph.initialize()
    solver = LPSolver(graph)
    solver.solve()
