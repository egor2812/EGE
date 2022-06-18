f = open('24.txt')
f = f.read()
c = 0
lst = []
f = f.replace('AC','AB')
f = f.replace('AB','x')
for i in f:
    if i == 'x':
        c+=1
    else:
        lst.append(c)
        c=0
print(max(lst))