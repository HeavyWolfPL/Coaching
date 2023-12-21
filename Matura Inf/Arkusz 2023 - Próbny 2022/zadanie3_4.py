with open("Dane_2212/liczby_przyklad.txt", mode="r") as file:
    dane = file.readlines()

alfabet = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0
}


for liczba in dane:
    liczba = int(liczba)
    liczba = hex(liczba)

    for i in range(2, len(liczba)):
        litera = liczba[i]
        litera = litera.upper()
        alfabet[litera] = alfabet[litera]+1

print(alfabet)