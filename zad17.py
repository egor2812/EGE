count = 0
maxc = 0
for i in range(1016, 7938):
    if i % 3 == 0 and i % 70 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        count += 1
        maxc = max(i, maxc)
print(count, maxc)
