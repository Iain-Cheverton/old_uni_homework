import numpy as np


def rolling_dice(n, val):
    if n > 10 ** 6:
        return None
    dice1 = np.random.randint(1, 7, n + 1)
    count = 0
    for i in range(n):
        if dice1[i] == dice1[i + 1] == val:
            count += 1
    return count


def test_throw(n, val):
    if isinstance(val, int) and isinstance(n, int) and n <= 10 ** 6 and 0 < val < 7:
        return rolling_dice(n, val) / n


print(test_throw(10 ** 6, 6))
