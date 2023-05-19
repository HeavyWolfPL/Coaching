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
    
amplituda = 0
dataAmplitudy = 0
for dzien in dni:
    maks = -10000.0
    minimalna = 10000.0

    for godzina in dzien:
        godzina = godzina.split("\t")

        data = godzina[0].split(" ")
        temperatura = godzina[1]
        temperatura = float(temperatura.replace(",", "."))

        if temperatura > maks:
            maks = temperatura

        if temperatura < minimalna:
            minimalna = temperatura

    if amplituda < maks-minimalna:
        amplituda = maks-minimalna
        dataAmplitudy = data[0]
        

print(amplituda, dataAmplitudy)


    
