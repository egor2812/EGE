# Parallelizing using Pool.map()
import multiprocessing as mp
from multiprocessing import freeze_support
import numpy as np
from time import time

pool = mp.Pool(mp.cpu_count())
# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()

# Parallelizing with Pool.starmap_async()


results = []


def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count


freeze_support()

results = pool.map_async(howmany_within_range_rowonly, [row for row in data]).get()

# With map, use `howmany_within_range_rowonly` instead
# results = pool.map_async(howmany_within_range_rowonly, [row for row in data]).get()

pool.close()
print(results[:10])
# > [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
