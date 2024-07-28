import numpy as np


def compute_mean(X):
    return np.mean(X)


def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    for x in X:
        variance += (x - mean) ** 2
    variance /= len(X)
    return np.sqrt(variance)


X = [171, 176, 155, 167, 169, 182]
print(compute_std(X))
