plik = open("zalaczniki/statki.txt", mode='r', encoding='utf-8')
statki = []

plik = plik.read()

for statek in plik:
    print(statek)
    statek = statek.split(';')
    statki.append(statek)

print(statki)