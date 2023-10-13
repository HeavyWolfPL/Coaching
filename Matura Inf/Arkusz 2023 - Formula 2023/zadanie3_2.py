plik = open("Dane_2305/pi.txt", "r")
dane = plik.readlines()

lista = []

najczestsza = [0, 0]
najrzadsza = [0, 999999999]

for i in range(0, len(dane)-1):
    liczba = dane[i][0] + dane[i+1][0]
    liczba = int(liczba)

    istnieje = False
    for para in lista:
        if para[0] == liczba:
            para[1] += 1
            istnieje = True
            break

    if istnieje == False:
        lista.append([liczba, 1])

for i in lista:
    if i[1] > najczestsza[1]:
        najczestsza = i
    if i[1] < najrzadsza[1]:
        najrzadsza = i

print(f"Najczestsza liczba - {najczestsza[0]}, ilosc - {najczestsza[1]}")
print(f"Najrzadsz liczba - {najrzadsza[0]}, ilosc - {najrzadsza[1]}")

plik = open("wyniki3.txt", "a")
plik.write(f"3.2 {najrzadsza[0]} {najrzadsza[1]}, {najczestsza[0]} {najczestsza[1]}\n")