with open("zalaczniki/brenna.txt") as file:
    data = file.readlines()

dni = []
j = 0
dzien = []
for i in range(1, len(data)):
    dzien.append(data[i])
    j += 1

    if j == 24:
        j = 0
        dni.append(dzien)
        dzien = []

wyjazdy = 0
rekordWyjazdow = 0
rekordDzien = ''

opadySniegu = 0.0

for dzien in dni:
    wyjazdyDzien = 0
    data = ''
    for godzina in dzien:
        godzina = godzina.split("\t")
        data = godzina[0].split(" ")
        temperatura = float(godzina[1].replace(",", "."))
        opad = float(godzina[2].replace(",", "."))

        if opadySniegu >= 4:
            opadySniegu = 0.0
            wyjazdy += 1
            wyjazdyDzien += 1
            continue
        
        if (temperatura > 0) and (opad > 0):
            opadySniegu = 0
            continue
        else:
            opadySniegu += opad

    if wyjazdyDzien > rekordWyjazdow:
        rekordWyjazdow = wyjazdyDzien
        rekordDzien = data[0]
        

print(f"""
Wyjazdy - {wyjazdy}, 
Najwieksza liczba wyjazdów - {rekordWyjazdow}, 
Dzień - {rekordDzien}"""
)



    
