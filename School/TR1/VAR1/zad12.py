for i in range(200, 1000):
    a = '1' * i
    while '111' in a or '222' in a:
        a = a.replace('111', '22', 1)
        a = a.replace('222', '1', 1)
    if not '2' in a:
        print(a, i)