f = open('17.txt')
a = []
mina = 1000000
maxs = 0
counter = 0
for i in f:
    a.append(i[:-1])
for i in range(len(a)):
    if int(a[i]) % 17 == 0:
        mina = min(mina,int(a[i]))

for i in range(0,len(a)-1):
    if (int(a[i]) % mina == 0) or (int(a[i+1]) % mina == 0):
        counter+=1
        maxs = max(maxs,int(a[i])+int(a[i+1]))
print(counter,maxs)