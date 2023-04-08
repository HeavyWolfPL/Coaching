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

planszeRownowaga = 0
najmniejszaLiczba = 999

for plansza in lista_plansz:
    male = []
    wielkie = []

    # for i, linia in enumerate(plansza):
    #     plansza[i] = linia.replace('.', '').replace('\n', '')
    # Powyższy fragment jest nam generalnie zbędny - możemy po prostu usunąć więcej znaków, tak jak poniżej
    plansza = str(plansza).replace("[", "").replace("]", "").replace("\\n", "").replace(".", "").replace("'", "").replace(", ", "")

    for literka in plansza:
        if literka.islower() == True:
            male.append(literka)
        else:
            wielkie.append(literka)

    for i, literka in enumerate(wielkie):
        wielkie[i] = literka.lower()

    if sorted(male) == sorted(wielkie):
        planszeRownowaga += 1
        if len(male) + len(wielkie) < najmniejszaLiczba:
            najmniejszaLiczba = len(male) + len(wielkie)

print(planszeRownowaga, najmniejszaLiczba)
with open('wyniki/zadanie1_3.txt', 'w') as f:
    f.write(f"{planszeRownowaga} {najmniejszaLiczba}")