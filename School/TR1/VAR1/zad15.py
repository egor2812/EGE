for a in range(1000):
    f = True
    for x in range(1000):
        if not ((x & 85 == 0) <= ((x & 54 != 0) <= (x & a != 0))):
            f = False
            break
    if f:
        print(a)
        break
