import numpy
from numpy import int32
import multiprocessing as mp

h = numpy.empty(1000000000, dtype=int32)
print(h.size, len(h))


def f(a):
    arg = a
    result = 0
    if h[a] == 0:
        while a & 1 == 0 and a > 0:
            a >>= 1
        if a == 0:
            result = 0
        elif a % 2 != 0:
            result = f(a - 1) + 1
        h[a] = result
        h[arg] = result
    else:
        result = h[a]
    return result


count = 0


for i in range(1000000000):
    if f(i) == 2:
        count += 1
    if i % 1000000 == 0:
        print(i / 1000000)
print(count)
