import numpy as np


def gaussian_noise(image, mean=0, var=1):
    n_rows, n_cols = image.shape
    noise = np.random.normal(mean, var**0.5, (n_rows, n_cols))
    noise = noise.reshape((n_rows, n_cols))
    result = (noise + image).astype(np.uint8)
    # print(np.any(result[result > 255]))
    # result = result.astype(np.uint8)
    # result[result > 255] = 255
    # result[result < 0] = 0
    return result


def salt_and_pepper_noise(image, sp=0.5, p=0.04):
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(p * image.size * sp)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    out[coords] = 255

    # Pepper mode
    num_pepper = np.ceil(p * image.size * (1. - sp))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    out[coords] = 0
    return out.astype(np.uint8)


