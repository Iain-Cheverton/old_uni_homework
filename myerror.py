from scipy import integrate
import math


def gauss(x, m, s):
    return 1 / (math.sqrt(2 * math.pi) * s) * math.e ** ((-((m - x) ** 2)) / (2 * s ** 2))


def myerror_function(low, hi, m, s):
    f = lambda x: gauss(x, m, s)
    return integrate.quad(f, low, hi)


print(myerror_function(1, 2, 3, 4))
