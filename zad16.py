h = {}


def f(a):
    result = 0
    if h.get(a) is None:
        if a == 0:
            result = 0
        elif a % 2 != 0:
            result = f(a - 1) + 1
        elif a % 2 == 0:
            result = f(a // 2)
        h[a] = result
    else:
        result = h[a]
    return result

count = 0

for i in range(10000000):
     if f(i) == 2:
         count += 1

print(h)
