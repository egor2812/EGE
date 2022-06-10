

for A in range(1, 1001):
    p = True
    for x in range(1,1000):
        f = (A % 7 == 0) and ((240 % x == 0) <= ((not (A % x == 0)) <= (not (780 % x == 0))))
        if f == False:
            p = False
            break
    if p == True:
        print(A)
