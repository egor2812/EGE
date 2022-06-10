print('x y z | f')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            f = z and not (y == z) and (y <= x)
            if f == 1:
                print(x, y, z, f)
