plansze = []

with open("zalaczniki/szachy.txt") as plik:
# with open("zalaczniki/szachy_przyklad.txt") as plik:
    plansze = plik.readlines()

    plansza_pojedyncza = []
    lista_plansz = []

    i = 0
    for linia in plansze:
        if i == 8:
            lista_plansz.append(plansza_pojedyncza)
            plansza_pojedyncza = []
            i = 0
            continue
        i += 1
        plansza_pojedyncza.append(linia)
    lista_plansz.append(plansza_pojedyncza)

pustePlansze = 0
maxPusteKolumny = 0

for plansza in lista_plansz:
    if plansza == []: # Bardzo ważne, wytłumaczone w instrukcji
        continue
    pusteKolumny = 0

    for kolumna in range(8): # nasze X na układzie współrzędnych
        pusta = True
        for wiersz in range(8): # nasze Y
            if plansza[wiersz][kolumna] != ".":
                pusta = False
                break

        if pusta:
            pusteKolumny += 1

    if pusteKolumny != 0:
        pustePlansze += 1

    if pusteKolumny > maxPusteKolumny:
        maxPusteKolumny = pusteKolumny
                
print(pustePlansze, maxPusteKolumny)
with open('wyniki/zadanie1_3.txt', 'w') as f:
    f.write(f"{pustePlansze} {maxPusteKolumny}")