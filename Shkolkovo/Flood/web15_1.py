for A in range(0, 100):
    p = True
    for x in range(0, 100):
        for y in range(0, 100):
            f = (75 != 2 * x + 3 * y) or (A > 3 * x) or (A > 2 * y)
            if f == False:
                p = False
                break
        if (p == False):
            break
    if p == True:
        print(A)
