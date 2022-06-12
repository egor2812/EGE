def f(x, y, a):
    return (x * y < a) or (x >= 16) or (x < 5 * y)


for a in range(-1000, 1000):
    podhodit = True
    for x in range(1, 100):
        for y in range(1, 100):
            if f(x, y, a) == False:
                podhodit = False
                break
        if not podhodit:
            break
    if podhodit:
        print(a)
        break
