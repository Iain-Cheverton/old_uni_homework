import numpy as np
import math


def lorentz_test(mat):
    transpose = np.ndarray.transpose(mat)
    if len(transpose) == len(mat):
        det = np.linalg.det(mat)
        if 0.99 < det < 1.01:
            n = np.mat((np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])))
            y = transpose * n * mat
            for i in range(4):
                for j in range(4):
                    if not n[i, j] - 0.01 <= y[i, j] <= n[i, j] + 0.01:
                        return False
            return True
        else:
            return False
    else:
        return False


print(
    lorentz_test(np.mat((np.array([[math.sqrt(2), -1, 0, 0], [-1, math.sqrt(2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],]))))
)
