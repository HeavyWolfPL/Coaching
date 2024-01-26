with open("DANE/anagram.txt", mode="r") as file:
    dane = file.readlines()

naj_roznica = 0

for i, line in enumerate(dane):
    line = line.replace("\n", "")

    if i == 0:
        continue

    poprz = dane[i-1].replace("\n", "")
    poprz = int(poprz, 2)
    akt = line
    akt = int(akt, 2)

    roznica = akt-poprz
    roznica = str(roznica).replace("-", "")
    roznica = int(roznica)

    if naj_roznica < roznica:
        naj_roznica = roznica

# naj_roznica = str(bin(naj_roznica))[2::]
naj_roznica = str(bin(naj_roznica))
slowo = []
for i, lit in enumerate(naj_roznica):
    if i < 2:
        continue

    slowo.append(lit)

naj_roznica = "".join(slowo)
print(naj_roznica)

