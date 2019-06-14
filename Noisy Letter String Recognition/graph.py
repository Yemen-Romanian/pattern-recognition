import numpy as np
from generator import TTIGenerator


class Graph:

    def __init__(self, alphabet, string):
        self.alphabet = alphabet
        self.string = string
        self.objects_number = string.shape[1]
        self.vertix_weights = np.zeros((self.objects_number, len(alphabet)))
        self.edge_weights = np.inf * np.ones((self.objects_number, self.objects_number,
                                              len(alphabet), len(alphabet)))

        self.mapping = {i: char for i, char in enumerate(self.alphabet)}

    def initialize(self):
        for i in np.arange(self.objects_number)[::-1]:
            for char in self.mapping:
                char_image = self.alphabet[self.mapping[char]]
                char_width = char_image.shape[1]
                if i - char_width < 0:
                    continue

                self.edge_weights[i - char_width, i, :, char] = np.sum((char_image
                                                                        - self.string[:, i - char_width:i])**2)


if __name__ == '__main__':
    generator = TTIGenerator('images')
    string = generator.add_noise(generator.text_to_image('ABCABC__AA___C'))
    graph = Graph(generator.alphabet, string)
    graph.initialize()
    print('Done!')
