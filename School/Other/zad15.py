def f(x, A):
    return (((x % 3 == 0) <= (not (x % 5 == 0))) or (x + A >= 70))


for A in range(1, 100):
    podhodit = True
    for x in range(1, 100):
        if f(x, A) == False:
            podhodit = False
    if podhodit:
        print(A)
