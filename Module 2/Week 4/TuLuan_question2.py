import numpy as np


def compute_median(X):
    size = len(X)
    X = np.sort(X)
    if size % 2 == 0:
        return (X[size // 2 - 1] + X[size // 2]) / 2
    else:
        return X[size // 2]


X = [1, 5, 4, 4, 9, 13]
print("Median: ", compute_median(X))
