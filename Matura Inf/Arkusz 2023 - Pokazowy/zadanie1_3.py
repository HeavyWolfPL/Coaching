plansze = []

# with open("zalaczniki/szachy.txt") as plik:
with open("zalaczniki/szachy_przyklad.txt") as plik:
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

bialySzach = 0
czarnySzach = 0

for plansza in lista_plansz:
    czarnyKrol = []
    czarnaWieza1 = []
    czarnaWieza2 = []

    bialyKrol = []
    bialaWieza1 = []
    bialaWieza2 = []
    for x, wiersz in enumerate(plansza):
        for y, kolumna in enumerate(wiersz):
            if kolumna == 'k':
                czarnyKrol = [x, y]
            elif kolumna == 'K':
                bialyKrol = [x, y]
            elif kolumna == 'w':
                if czarnaWieza1 == []:
                    czarnaWieza1 = [x, y]
                else:
                    czarnaWieza2 = [x, y]
            elif kolumna == 'W':
                if bialaWieza1 == []:
                    bialaWieza1 = [x, y]
                else:
                    bialaWieza2 = [x, y]

    if (bialyKrol != []) and (czarnaWieza1 != []):
        osPlanszy = 0
        if bialyKrol[0] == czarnaWieza1[0]:
            osPlanszy = 'x'
            wieza = 1
        elif bialyKrol[1] == czarnaWieza1[1]:
            osPlanszy = 'y'
            wieza = 1

        # TODO: Zamiast deklarować wieza = 2, zmieńmy po prostu wartość czarnaWieza1
        if (czarnaWieza2 != []) and (osPlanszy == 0):
            if bialyKrol[0] == czarnaWieza2[0]:
                osPlanszy = 'x'
                wieza = 2
            elif bialyKrol[1] == czarnaWieza2[1]:
                osPlanszy = 'y'
                wieza = 2

        start = None
        koniec = None
        if osPlanszy == 'x':
            if wieza == 1:
                start = min(bialyKrol[1], czarnaWieza1[1])
                koniec = max(bialyKrol[1], czarnaWieza1[1])
            if wieza == 2:
                start = min(bialyKrol[1], czarnaWieza2[1])
                koniec = max(bialyKrol[1], czarnaWieza2[1])
        elif osPlanszy == 'y':
            if wieza == 1:
                start = min(bialyKrol[0], czarnaWieza1[0])
                koniec = max(bialyKrol[0], czarnaWieza1[0])
            if wieza == 2:
                start = min(bialyKrol[0], czarnaWieza2[0])
                koniec = max(bialyKrol[0], czarnaWieza2[0])


        if start != None:
            pustaLinia = True
            for i in range(start, koniec):
                if osPlanszy == 'x':
                    if plansza[bialyKrol[0]][i] not in ['.', 'K']:
                        pustaLinia = False
                if osPlanszy == 'y':
                    if plansza[i][bialyKrol[1]] not in ['.', 'K']:
                        pustaLinia = False

            if pustaLinia:
                czarnySzach += 1

    if (czarnyKrol != []) and (bialaWieza1 != []):
        osPlanszy = 0
        if czarnyKrol[0] == bialaWieza1[0]:
            osPlanszy = 'x'
            wieza = 1
        elif czarnyKrol[1] == bialaWieza1[1]:
            osPlanszy = 'y'
            wieza = 1

        if bialaWieza2 != [] and (osPlanszy == 0):
            if czarnyKrol[0] == bialaWieza2[0]:
                osPlanszy = 'x'
                wieza = 2
            elif czarnyKrol[1] == bialaWieza2[1]:
                osPlanszy = 'y'
                wieza = 2

        start = None
        koniec = None
        if osPlanszy == 'x':
            if wieza == 1:
                start = min(czarnyKrol[1], bialaWieza1[1])
                koniec = max(czarnyKrol[1], bialaWieza1[1])
            if wieza == 2:
                start = min(czarnyKrol[1], bialaWieza2[1])
                koniec = max(czarnyKrol[1], bialaWieza2[1])
        elif osPlanszy == 'y':
            if wieza == 1:
                start = min(czarnyKrol[0], bialaWieza1[0])
                koniec = max(czarnyKrol[0], bialaWieza1[0])
            if wieza == 2:
                start = min(czarnyKrol[0], bialaWieza2[0])
                koniec = max(czarnyKrol[0], bialaWieza2[0])

        if start != None:
            pustaLinia = True
            for i in range(start, koniec):
                if osPlanszy == 'x':
                    if plansza[czarnyKrol[0]][i] not in ['.', 'k']:
                        pustaLinia = False
                if osPlanszy == 'y':
                    if plansza[i][czarnyKrol[1]] not in ['.', 'k']:
                        pustaLinia = False

            if pustaLinia:
                bialySzach += 1

print(bialySzach, czarnySzach)
with open('wyniki/zadanie1_3.txt', 'w') as f:
    f.write(f"{bialySzach} {czarnySzach}")