import numpy as np


def polyfit_file(name, degree):
    data = np.loadtxt(name)
    x = data[:, 0]
    y = data[:, 1]
    return np.polyfit(x, y, degree)


print(polyfit_file("fitdata.txt", 2))
