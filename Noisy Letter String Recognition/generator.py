import os
import numpy as np
import matplotlib.pyplot as plt


class TTIGenerator:

    def __init__(self, path_to_images, font=1):
        self.im_height = 28
        self.im_width = 28

        self.path_to_images = path_to_images
        self.alphabet = {letter: 255 - plt.imread(os.path.join(path_to_images, letter, '{}.png'.format(font)))
                         for letter in os.listdir(path_to_images)}
        self.alphabet['_'] = 255 * np.ones((self.im_height, 1))

    def text_to_image(self, text):
        im_width = 0
        for char in text:
            if char == '_':
                im_width += 1
            else:
                im_width += self.im_width

        im_string = np.zeros((self.im_height, im_width))

        i = 0
        for char in text:
            char_image = self.alphabet[char]
            im_string[:, i:i+char_image.shape[1]] = char_image
            i += char_image.shape[1]

        return im_string

    def add_noise(self, image, mu=0, sigma=1):
        noise = np.random.normal(mu, sigma, image.shape)
        return np.round(image + noise)


if __name__ == '__main__':
    gen = TTIGenerator('images')
    image = gen.text_to_image('A_________B__CAB___A')
    image = gen.add_noise(image)
    plt.imshow(image, cmap='gray')
    plt.savefig('image.png')


