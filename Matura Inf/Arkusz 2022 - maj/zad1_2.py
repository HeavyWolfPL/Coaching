ciag = (1, 3, 1)

def element_w_liscie(element, lista):
    for x in lista:
        if element == x:
            return True
        else:
            return False
    


liczby = []
podmianki = 0
for liczba in ciag:
    if element_w_liscie(liczba, liczby):
        podmianki += 1
    elif liczba > len(ciag) or liczba <= 0:
        podmianki += 1
    else:
        liczby.append(liczba)

# print(liczby, podmianki)
print(podmianki)