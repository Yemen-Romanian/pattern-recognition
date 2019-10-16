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
    sampling_iter = settings['iterations']['sampling']
    drop = settings['iterations']['drop']
    save_step = settings['iterations']['step']

    labels = np.arange(
        settings['labels']['min'],
        settings['labels']['max'] + 1
    )

    eps = settings['cost']['epsilon']
    beta = settings['cost']['beta']

    input_image = generate_image(
        (width, height),
        'test',
        eps=eps,
        beta=beta,
        gen_iter=gen_iter,
        labels=labels
    )

    print('Starting sampling...')
    zero_frequences = np.zeros(input_image.shape)
    ones_frequences = np.zeros(input_image.shape)
    j = 0
    for i in range(sampling_iter):
        input_image = step(input_image, labels, eps, beta)
        if i > drop and i % save_step == 0:
            zero_frequences += np.logical_xor(input_image, np.ones(input_image.shape))
            ones_frequences += np.logical_xor(input_image, np.zeros(input_image.shape))
            j += 1

    result_image = ones_frequences > zero_frequences
    plt.imshow(result_image, cmap='gray')
    plt.title('Result image')
    plt.savefig('result')

    
if __name__ == '__main__':
    main('settings.json')