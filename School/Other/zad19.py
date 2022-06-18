from functools import lru_cache


def moves(h):
    x, y = h
    return (x + 1, y), (x * 2, y), (x, y + 1), (x, y * 2)


@lru_cache(None)
def f(h):
    if sum(h) >= 223:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return ('WIN1')
    if all(f(x) == 'WIN1' for x in moves(h)):
        return ('LOSE1')
    if any(f(x) == 'LOSE1' for x in moves(h)):
        return ('WIN2')
    if all(f(x) == 'WIN1' or f(x) == 'WIN2' for x in moves(h)):
        return ('LOSE2')


for i in range(1,224):
    h = (17, i)
    print(f(h), i)
