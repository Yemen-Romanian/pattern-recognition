from floyd_warshall import floyd_warshall
import pandas as pd
import numpy as np
import argparse

# # - black symbol
alphabet = ['a', 'b', 'c', '#']
index = pd.Index(alphabet, name="rows")
columns = pd.Index(alphabet, name="columns")

# you may provide all penalties in this matrix
# 0-1 penalties are the default ones
penalties = np.array([[0, 1, 1, 1], 
                      [1, 0, 1, 1],
                      [1, 1, 0, 1],
                      [1, 1, 1, 0]])

# getting optimal penalties by Floyd-Warshall algorithm
opt_penalties = floyd_warshall(penalties)

# created dataframes just for being able to have string indices
opt_penalties = pd.DataFrame(data=opt_penalties,
                             index=index,
                             columns=columns)


def levenshtein_distance(x, y):
    dists = np.zeros((len(y), len(x)))
    dists[0, 0] = 0
    
    for i in range(1, dists.shape[0]):
        dists[i, 0] = dists[i-1, 0] + opt_penalties.loc['#', y[i]]

    for j in range(1, dists.shape[1]):
        dists[0, j] = dists[0, j-1] + opt_penalties.loc[x[j], '#']

    for i in range(1, len(y)):
        for j in range(1, len(x)):
            dists[i, j] = min(dists[i-1, j] + opt_penalties.loc['#', y[i]],
                              dists[i, j-1] + opt_penalties.loc[x[j], '#'],
                              dists[i-1, j-1] + opt_penalties.loc[x[j], y[i]])

    return dists[-1, -1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('y', metavar='X', type=str,
                        help='String for recognition')

    parser.add_argument('x', metavar='Y', type=str,
                        help='String for recognition')

    args = parser.parse_args()

    x = args.x
    y = args.y
    print(levenshtein_distance(x, y))
