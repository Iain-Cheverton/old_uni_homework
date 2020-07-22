import math


def mean_rms_file(name):
    f = open(name, "r")
    x = f.read()
    y = x.split("\n")
    y.remove("")
    for i in range(len(y)):
        y[i] = float(y[i])
    mean = sum(y) / len(y)
    z = y.copy()
    for i in range(len(z)):
        z[i] = z[i] * z[i]
    rms = math.sqrt(sum(z) / len(z))
    return mean, rms


print(mean_rms_file("data1.txt"))
