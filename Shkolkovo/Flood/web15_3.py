for A in range(1,1000):
    p = True
    for x in range(1,1000):
        f = (x&A !=0) and (x&48 == 0) and (x&27 == 0)
        if f == True:
            p = False
            break
    if (p == True ):
        print(A)