def decimalToBin(n):
    n = int(n)
    binarna = ''
    while n > 0:
        binarna = str(n % 2) + binarna
        n //= 2
    return binarna

def funkcja(n):
    blok = ''
    lista = []

    for i, x in enumerate(n):
        x = int(x)

        if n[i] != n[i-1] and blok != '':
            lista.append(blok)
            blok = ''
            blok = str(blok) + str(x)
        else:
            blok = str(blok) + str(x)

    if blok != '':
        lista.append(blok)
    return lista
    
plik = open(file='Dane_2305/bin.txt', mode='r')
dane = plik.readlines()
ilosc = 0

for liczba in dane:
    liczba = liczba.replace('\n', '')
    wynik = funkcja(liczba)

    if len(wynik) <= 2:
        ilosc += 1

print(ilosc)

