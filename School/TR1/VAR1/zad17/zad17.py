f = open('17.txt')
a = []
parcount = 0
parmaxsum = 0
for i in f:
    a.append(int(i))
for i in range(len(a)-1):
    if ((a[i] % 3 == 0) or (a[i+1] % 3 == 0)) and ((a[i]+a[i+1]) % 5 == 0):
        parcount +=1
        parmaxsum = max(parmaxsum,a[i]+a[i+1])
print(parcount,parmaxsum)