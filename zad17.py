
def zad1(count, maxc):
    for i in range(1016, 7938):
        if i % 3 == 0 and i % 70 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
            count += 1
            maxc = max(i, maxc)
    return count, maxc


def zad2(count, maxc):
    for i in range(1033, 7738):
        if i % 5 == 0 and i % 11 != 0 and i % 17 != 0 and i % 19 != 0 and i % 23 != 0:
            count += 1
            maxc = max(i, maxc)
    return count, maxc


def zad3(count, maxc):
    for i in range(1012, 9639):
        if i % 3 == 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
            count += 1
            maxc = max(i, maxc)
    return count, maxc


def zad4(count, maxc):
    for i in range(3201, 12877):
        if i % 4 == 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0 and i % 19 != 0:
            count += 1
            maxc = max(i, maxc)
    return count, maxc


def zad5(count, maxc):
    for i in range(1100, 11001):
        if i % 6 == 0 and i % 7 != 0 and i % 13 != 0 and i % 17 != 0 and i % 23 != 0:
            count += 1
            maxc = max(i, maxc)
    return count, maxc


def zad6(count, maxc):
    for i in range(1512, 13203):
        if i % 7 == 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 23 != 0:
            count += 1
            maxc = max(i, maxc)
    return count, maxc


def zad7(count, maxc):
    for i in range(1606, 9681):
        if i % 11 == 0 and i % 7 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
            count += 1
            maxc = max(i, maxc)
    return count, maxc


def zad8(count):
    for i in range(1200, 11201):
        if i % 5 == 0 and i % 7 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
            count += 1
            if(count==1): maxc = i
    return count, maxc


def zad9(count):
    for i in range(200, 9121):
        if i % 8 == 0 and i % 7 != 0 and i % 11 != 0 and i % 17 != 0 and i % 19 != 0:
            count += 1
            if(count==1): maxc = i
    return count, maxc


def zad10(count):
    for i in range(1107, 9505):
        if i % 9 == 0 and i % 7 != 0 and i % 15 != 0 and i % 17 != 0 and i % 19 != 0:
            count += 1
            if(count==1): maxc = i
    return count, maxc


print(zad10(0))

