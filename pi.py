import random
import math


def MCint_pi(n):
    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if math.sqrt(x * x + y * y) <= 1:
            count += 1
    return 4 * count / n


print(MCint_pi(1000000))
