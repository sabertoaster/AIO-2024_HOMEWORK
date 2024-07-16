# a) Do dai cua vector
import numpy as np


def compute_vector_length(v):
    len_of_vector = np.linalg.norm(v)
    return len_of_vector


# b) Phep tich vo huong
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


# c) Nhan ma tran voi ma tran
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


# d) Nhan ma tran voi ma tran
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


# e) Ma tran nghich dao
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


if __name__ == "__main__":
    # generate test case and use pre-defined function to check the result
    matrix = np.array([[1, 2], [3, 4]])
    vector = np.array([1, 2])
    print(compute_vector_length(vector))
    print(compute_dot_product(vector, vector))
    print(matrix_multi_vector(matrix, vector))
    print(matrix_multi_matrix(matrix, matrix))
    print(inverse_matrix(matrix))
