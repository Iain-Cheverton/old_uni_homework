def dictionary_values(d):
    newlist = []
    for keys in d:
        value = d[keys]
        newlist.append(value)
    return newlist


def mysum(container):
    if isinstance(container, (tuple, list, set)):
        return sum(container)
    elif isinstance(container, dict):
        return sum(dictionary_values(container))


a = (12, 45, 67)
b = [13, 46, 68]
c = {14, 47, 69}
d = {1: 15, 2: 48, 3: 70, 4: -1}
print(mysum(a), mysum(b), mysum(c), mysum(d))
