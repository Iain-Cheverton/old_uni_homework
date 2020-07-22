import numpy as np


def flip_coin(n):
    if n <= 10 ** 6:
        data = np.random.random_integers(1, 2, n)
        heads = 0
        for i in range(n):
            if data[i] == 1:
                heads += 1
        return heads


print(flip_coin(10000000))
