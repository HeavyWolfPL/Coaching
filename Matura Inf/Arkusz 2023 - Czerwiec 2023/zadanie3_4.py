with open("DANE/anagram.txt", mode="r") as file:
    dane = file.readlines()

def znajdz_cyfry(liczba):
    cyfry = []
    for c in liczba:
        if c not in cyfry:
            cyfry.append(c)

    return cyfry

for i, line in enumerate(dane):
    line = line.replace("\n", "")

    dane[i] = int(line, 2)



brak_zer = 0
najw_suma = 0
najw_suma_liczba = 0
for line in dane:
    if "0" not in str(line):
        brak_zer += 1
    
    cyfry = znajdz_cyfry(str(line))
    suma = 0
    for c in cyfry:
        suma += int(c)

    if suma > najw_suma:
        najw_suma = suma
        najw_suma_liczba = line

print(brak_zer)
print(najw_suma_liczba)
