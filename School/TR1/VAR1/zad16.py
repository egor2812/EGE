def f(x):
    if x == 0: return(0)
    if x>0 and x %2 == 0:
        return f(x/2)
    if x % 2 !=0:
        return 1+f(x-1)
counter = 0
for i in range(1,501):
    if f(i) == 8:
        counter +=1
print(counter)
