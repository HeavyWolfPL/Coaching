lista = [3, 3, 3, 2, 2, 1, 1, 1, 6]
ciag = []

ilosc = 0
i = 0
for x in lista:
    # Pierwszy element, bo nie ma porównania
    if i == 0:
        ilosc += 1

    # ostatni element w liście
    elif i == len(lista)-1:
        if lista[i] != lista[i-1]:
            ciag.append(ilosc)
            ciag.append(lista[i-1])
            ilosc = 1
        else:
            ilosc += 1
        ciag.append(ilosc)
        ciag.append(lista[i])

    # elementy środkowe
    elif i != 0:
        if lista[i] == lista[i-1]:
            ilosc += 1
        else:
            ciag.append(ilosc)
            ciag.append(lista[i-1])
            ilosc = 1
    
    # Tutaj by liczyć elementy
    i += 1

print(len(ciag))