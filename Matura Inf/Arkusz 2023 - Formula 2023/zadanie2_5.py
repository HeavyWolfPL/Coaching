def decimalToBin(n):
    n = int(n)
    binarna = ''
    while n > 0:
        binarna = str(n % 2) + binarna
        n //= 2
    return binarna

def binToDec(n):
    n = int(n, 2)
    return n

plik = open(file="Dane_2305/bin.txt", mode='r')
dane = plik.readlines()
wyniki = []

for n1 in dane:
    n1 = n1.replace('\n', '')
    n2 = binToDec(n1)
    n2 //= 2
    n2 = decimalToBin(n2)

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

    wynik = ''
    for i, liczba in enumerate(n1):
        if n1[i] == n2[i]:
            wynik = wynik + '0'
        elif n1[i] != n2[i]:
            wynik = wynik + '1'

    wyniki.append(wynik)


plik = open("wyniki2_5.txt", mode='w')

for x in wyniki:
    plik.write(str(x) + '\n')



