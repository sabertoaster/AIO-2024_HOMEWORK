import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


if __name__ == "__main__":
    matrix = np.array([[1, 2], [3, 4]])
    eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
    print(eigenvalues)
    print(eigenvectors)
