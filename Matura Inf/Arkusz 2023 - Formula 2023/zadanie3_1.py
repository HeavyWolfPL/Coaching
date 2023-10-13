plik = open("Dane_2305/pi.txt", "r")
dane = plik.readlines()

ilosc = 0
for i in range(0, len(dane)-1):
    liczba = dane[i][0] + dane[i+1][0]
    liczba = int(liczba)
    if liczba > 90:
        ilosc += 1

print(ilosc)

plik = open("wyniki3.txt", "a")
plik.write(f"3.1 {ilosc}\n")