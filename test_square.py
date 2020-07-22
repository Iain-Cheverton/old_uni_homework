import numpy as np


def test_square(matrix):
    y = np.ndarray.transpose(matrix)
    if len(y) == len(matrix):
        return True
    else:
        return False


print(test_square(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
