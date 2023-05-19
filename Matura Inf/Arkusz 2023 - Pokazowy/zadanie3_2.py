a = 3
x = 3
M = 11

b = (a ** x) % M
print(b)

def funkcja(a, x, M):
    if x == 0:
        return 1
    if x % 2 == 0:
        w = funkcja(a, x / 2, M)
        return w*w % M
    if x % 2 == 1:
        w = funkcja(a, (x-1)/2, M)
        return a*w*w % M
    
b = funkcja(a, x, M)
print(b)

def funkcja2(a, x, M):
    w = 1
    z = a
    while x > 0:
        if x % 2 == 1:
            w = w * z % M
            z = z * z % M
            x = x / 2
    return w

b = funkcja2(a, x, M)
print(b)
