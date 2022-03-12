f = open('17.txt')
a = []
summ = 0
counter = 0
parcount = 0
parmax = 0
for i in f:
    a.append(int(i))
for i in a:
    if i % 2 == 0:
        summ += i
        counter += 1
sred = summ / counter
for i in range(0,len(a)-1):
    if a[i]%3==0 and a[i+1]<sred or a[i+1]%3==0 and a[i]<sred:
        parcount+=1
        parmax = max(parmax,a[i]+a[i+1])
print(parcount,parmax)
