from graph import Graph
from labeling_problem_solver import LPSolver
from generator import TTIGenerator
import argparse
import matplotlib.pyplot as plt


def demo(text, generator, eps):
    alphabet = generator.alphabet
    image_string = generator.text_to_image(text)
    image_string = generator.add_noise(image_string, epsilon=eps)
    graph = Graph(alphabet, image_string)
    graph.init_edges()
    solver = LPSolver(graph)
    result, min_path_weight = solver.solve()

    fig = plt.figure(figsize=(6, 4))
    columns = 1
    rows = 2

    result_image = generator.text_to_image(result)

    fig.add_subplot(rows, columns, 1)
    plt.imshow(image_string, cmap='gray')
    plt.title('Image with noise, epsilon = {}'.format(eps))

    fig.add_subplot(rows, columns, 2)
    plt.imshow(result_image, cmap='gray')
    plt.title('Denoised image')

    plt.show()
    fig.savefig('image_{}.png'.format(eps))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('string', metavar='String', type=str,
                        help='String for recognition')
    parser.add_argument('-f', '--font',
                        type=int, default=1, metavar='Font',
                        help="Letters's font, integer value from 1 to 1873 (default 1)")

    parser.add_argument('-e', '--epsilon', metavar='Epsilon',
                        type=float, default=0.5,
                        help="Noise parameter epsilon, float value from 0 to 1. Default 0.5")

    args = parser.parse_args()

    text, font, eps = args.string, args.font, args.epsilon
    path_to_images = 'images'

    generator = TTIGenerator(path_to_images, font)
    demo(text, generator, eps)
