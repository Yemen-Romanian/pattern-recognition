import numpy as np


def floyd_warshall(incidence_mat):
    n = incidence_mat.shape[0]
    dist = np.copy(incidence_mat)

    for k in np.arange(n):
        for i in np.arange(n):
            dist[i, :] = np.minimum(dist[i, :], dist[i, k] + dist[k, :])

    return dist

            
