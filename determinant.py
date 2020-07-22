import numpy as np


def determinant(matrix):
    x = np.linalg.det(matrix)
    return x


print(determinant(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
