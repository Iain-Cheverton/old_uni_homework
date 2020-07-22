import math


def trajectory(xdata, speed, angle):
    radians = math.radians(angle)
    y = []
    y_0 = 0
    for x in xdata:
        f = x * math.tan(radians) - 9.81 * x * x / (2 * speed ** 2 * math.cos(radians) ** 2) + y_0
        if f >= 0:
            y.append(f)
    return y


print(max(trajectory(range(100), 20, 45)))
