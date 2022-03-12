f = open('26.txt')
a = list(map(int, f.read(12).split()))
A = []
B = []


class Order(object):
    """docstring"""

    def __init__(self, string):
        """Constructor"""
        a = string.split()
        self.price = int(a[0])
        self.count = int(a[1])
        self.liter = a[2]
    def __repr__(self):
        return '(' + str(self.price) + '){' + str(self.count) + '}'



for i in f:
    if 'A' in i:
        A.append(Order(i))
    elif 'B' in i:
        B.append(Order(i))
A.sort(key=lambda b: b.price)
B.sort(key=lambda b: b.price)

