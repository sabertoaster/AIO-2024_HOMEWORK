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


def compute_correlation_coefficient(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0
    mean_X = compute_mean(X)
    mean_Y = compute_mean(Y)
    std_X = compute_std(X)
    std_Y = compute_std(Y)
    for i in range(N):
        numerator += (X[i] - mean_X) * (Y[i] - mean_Y)
    numerator /= N
    denominator = std_X * std_Y
    return np.round(numerator / denominator, 2)


X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation: ", compute_correlation_coefficient(X, Y))
