print('w x y z | f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x != y) <= ((x and w)==(z and not w))
                if f == 0:
                    print(w,x,y,z,f)