for j in range(1,10000):
    n = str(j)
    sum_c = 0
    sum_m = 0
    for i in n:
        if int(i) % 2 == 0:
            sum_c += int(i)
    for i in range(len(n)):
        if i % 2 != 0:
            sum_m += int(n[i])
    if abs(sum_c - sum_m) == 13:
        print(j)
    #print(abs(sum_c - sum_m))