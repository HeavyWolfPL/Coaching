with open(file="Dane_2205/liczby.txt", mode="r") as plik:
    dane = plik.readlines()


for i in range(0, len(dane)):
    dane[i] = dane[i].replace("\n", "")
    dane[i] = int(dane[i])

dane = sorted(dane)
print(dane)

# Pętla na pierwszą liczbe
trojki = []
piatki = []
for liczba1 in dane:

    for liczba2 in dane:
        if liczba2 <= liczba1:
            continue
        
        if (liczba2 % liczba1) == 0:
            for liczba3 in dane:
                if liczba3 <= liczba2:
                    continue

                if (liczba3 % liczba2) == 0 and (liczba3 % liczba1) == 0:
                    trojki.append([liczba1, liczba2, liczba3])

                    for liczba4 in dane:
                        if liczba4 <= liczba3:
                            continue

                        if (liczba4 % liczba3) == 0:
                            for liczba5 in dane:
                                if liczba5 <= liczba4:
                                    continue
                                
                                if (liczba5 % liczba4) == 0:
                                    piatki.append([liczba1, liczba2, liczba3, liczba4, liczba5])
                    
with open("trojki.txt", mode="w") as plik:
    for x in trojki:
        print(x)
        plik.write(f"{x[0]} {x[1]} {x[2]}\n")


print("-----------")
for x in piatki:
    print(x)
        
print("-----------")
print(len(trojki), len(piatki))

