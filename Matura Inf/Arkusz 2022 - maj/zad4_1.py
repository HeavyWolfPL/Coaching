with open(file="Dane_2205/przyklad.txt", mode="r") as plik:
    dane = plik.readlines()


liczby = 0
pierwsza = None

for liczba in dane:
    liczba = liczba.replace("\n", "")

    ostatni_index = len(liczba)-1
    
    if liczba[0] == liczba[ostatni_index]:
        liczby += 1
        if pierwsza == None:
            pierwsza = liczba


print(liczby, pierwsza)