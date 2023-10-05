# def decimalToBin(n):
#     return bin(n)[2:]

def decimalToBin(n):
    binarna = ''
    while n > 0:
        binarna = str(n % 2) + binarna
        n //= 2
    return binarna

print(decimalToBin(67))

def funkcja(n):
    blok = ''
    lista = []

    for i, x in enumerate(n):
        x = int(x)

        # I sposób
        # if x == 0 and blok != '':
        #     lista.append(blok)
        #     blok = ''
        # elif x == 1:
        #     blok = str(blok) + str(x)

        # II sposób
        if n[i] != n[i-1]:
            lista.append(blok)
            blok = ''
            blok = str(blok) + str(x)
        elif n[i] == n[i-1]:
            blok = str(blok) + str(x)

    if blok != '':
        lista.append(blok)
    return lista

wynik = funkcja(decimalToBin(67))

print(wynik)

print(len(wynik))
    

