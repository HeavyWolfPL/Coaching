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
    
godzinyOpad = 0
poczatekData = 0
koniecData = 0
iloscOpad = 0

tymczasGodziny = 0
tymczasPoczatek = 0
tymczasKoniec = 0
tymczasIlosc = 0
for dzien in dni:
    for godzina in dzien:
        godzina = godzina.split("\t")
        data = godzina[0].split(" ")
        opad = float(godzina[2].replace(",", "."))

        if tymczasGodziny == 0 and opad > 0:
            tymczasGodziny += 1
            tymczasPoczatek = data
            tymczasIlosc += opad
            tymczasKoniec = data

        elif opad > 0:
            tymczasKoniec = data
            tymczasGodziny += 1
            tymczasIlosc += opad

        elif opad <= 0:
            if tymczasGodziny > godzinyOpad:
                godzinyOpad = tymczasGodziny
                poczatekData = tymczasPoczatek
                koniecData = tymczasKoniec
                iloscOpad = round(tymczasIlosc)

                tymczasGodziny = 0
                tymczasPoczatek = 0
                tymczasIlosc = 0
                tymczasKoniec = 0
            else:
                tymczasGodziny = 0
                tymczasPoczatek = 0
                tymczasIlosc = 0
                tymczasKoniec = 0

print(f"""
Ilość godzin - {godzinyOpad}, 
Początek - {poczatekData}, 
Koniec - {koniecData}, 
Ilość opadów - {iloscOpad}"""
)



    
