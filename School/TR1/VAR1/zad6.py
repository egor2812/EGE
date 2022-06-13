counter = 0
for i in range(1,100000):
    s = i
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s = s + 13
        n = n * 2
    if n == 128:
        counter+=1
print(counter)