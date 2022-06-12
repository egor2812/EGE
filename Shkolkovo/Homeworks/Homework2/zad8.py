f = open('zad8.txt')
a = []
for i in f:
    a.append(int(i))
kolv = a[0]
a.sort()
counter = 0
maxim = [0,0]
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        counter +=1
    else:
        if counter > maxim[0]:
            maxim[0] = max(maxim[0],counter)
            maxim[1] = a[i]
        counter = 0
print(maxim)