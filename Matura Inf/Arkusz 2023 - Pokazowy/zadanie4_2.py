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
    
srednia = []
for i in range(0, 24):
    srednia.append([])

for dzien in dni:

    for godzina in dzien:
        godzina = godzina.split("\t")

        data = godzina[0].split(" ")
        data = int(data[1].replace(":00", ""))

        temperatura = godzina[1]
        temperatura = float(temperatura.replace(",", "."))

        srednia[data].append(temperatura)
        

for i, godzina in enumerate(srednia):
    suma = 0
    for temp in godzina:
        suma += temp

    suma /= len(godzina)
    srednia[i] = round(suma, 2)


for i, godzina in enumerate(srednia):
    print(f"{str(i).zfill(2)}:00 - {godzina}")


    
