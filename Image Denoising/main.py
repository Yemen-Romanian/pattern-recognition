from generate import generate_image
from gibbs_sampler import step
import json
import matplotlib.pyplot as plt
import numpy as np

def main(settings_file):
    with open(settings_file) as f:
        settings = json.load(f)
    
    width = settings['image']['width']
    height = settings['image']['height']

    gen_iter = settings['iterations']['generation']
    drop = settings['iterations']['drop']
    save_step = settings['iterations']['step']
    threshold = settings['iterations']['threshold']

    labels = np.arange(
        settings['labels']['min'],
        settings['labels']['max'] + 1
    )

    eps = settings['cost']['epsilon']
    beta = settings['cost']['beta']

    image = generate_image(
        (width, height),
        'test',
        eps=eps,
        beta=beta,
        gen_iter=gen_iter,
        labels=labels
    )

    print('Starting sampling...')
    zero_frequences = np.zeros(image.shape)
    ones_frequences = np.zeros(image.shape)

    ones_matrix = np.ones(image.shape)
    zeros_matrix = np.zeros(image.shape)
    i = 0
    while True:
        previous_image = np.copy(image)
        image = step(image, labels, eps, beta)

        percentage = np.sum(previous_image != image) * 100 / np.size(image) 
        if percentage <= threshold:
            break
        if i > drop and i % save_step == 0:
            zero_frequences += np.logical_xor(image, ones_matrix)
            ones_frequences += np.logical_xor(image, zeros_matrix)
        i += 1

    result_image = ones_frequences > zero_frequences
    plt.imshow(result_image, cmap='gray')
    plt.title('Result image')
    plt.savefig('result')

    
if __name__ == '__main__':
    main('settings.json')