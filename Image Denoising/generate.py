import numpy as np
import matplotlib.pyplot as plt
from gibbs_sampler import step
    
def generate_image(
        size, filename, labels, 
        eps=0.3, beta=1.0, gen_iter=1000
    ):

    image = np.random.randint(
        0, len(labels), 
        size=size
    )


    for i in range(gen_iter):
        image = step(image, labels)

    noise = np.random.rand(*image.shape) < eps
    noised_image = np.logical_xor(image, noise)

    plt.imshow(image, cmap='gray')
    plt.title('Generated image')
    plt.savefig(filename)
    plt.imshow(noised_image, cmap='gray')
    plt.title('Noised image')
    plt.savefig(filename + ' noised')

    return noised_image
