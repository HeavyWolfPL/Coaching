def decimalToBin(n):
    n = int(n)
    binarna = ''
    while n > 0:
        binarna = str(n % 2) + binarna
        n //= 2
    return binarna

def hexToDec(n):
    n = int(n, 16)
    return n

# n1 = decimalToBin(123)
# n2 = '101101'

n1 = '1010110'
n2 = decimalToBin(hexToDec('2D'))
dlugosc = 0

if len(n1) > len(n2):
    dlugosc = len(n1)
else:
    dlugosc = len(n2)

if len(n1) < dlugosc:
    for i in range(0, dlugosc-len(n1)):
        n1 = '0' + n1

if len(n2) < dlugosc:
    for i in range(0, dlugosc-len(n2)):
        n2 = '0' + n2
print(n1, n2)

wynik = ''
for i, liczba in enumerate(n1):
    if n1[i] == n2[i]:
        wynik = wynik + '0'
    elif n1[i] != n2[i]:
        wynik = wynik + '1'


def binToDec(n):
    n = int(n, 2)
    return n

print(wynik)
print(binToDec(wynik))


