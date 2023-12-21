with open("Dane_2212/liczby_przyklad.txt", mode="r") as file:
    dane = file.readlines()

def generuj(maks):
    pierwsze = []
    for i in range(2, maks):
        pierwsza = True
        for j in range(2, i):
            if i % j == 0:
                pierwsza = False
                break
        
        if pierwsza:
            pierwsze.append(i)
    return pierwsze

liczby = []
liczby_orig = []

for i in dane:
    i = int(i)
    kombinacje = 0
    pierwsze = generuj(i)
    for a in pierwsze:
        if (i-a) in pierwsze:
            kombinacje += 1

    if (kombinacje > 0) and (i not in liczby_orig):
        if kombinacje % 2 != 0:
            kombinacje //= 2
            kombinacje += 1
        else:
            kombinacje //= 2

        liczby.append([i, kombinacje])
        liczby_orig.append(i)

najwieksza = [0, 0]
najmniejsza = [0, 99999999999]

for x in liczby:
    if x[1] > najwieksza[1]:
        najwieksza = x

    if x[1] < najmniejsza[1]:
        najmniejsza = x

print(najwieksza[0], najwieksza[1])
print(najmniejsza[0], najmniejsza[1])