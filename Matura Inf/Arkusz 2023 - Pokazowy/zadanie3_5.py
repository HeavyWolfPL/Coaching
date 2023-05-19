with open("zalaczniki/liczby_przyklad.txt", mode="r") as file:
    data = file.readlines()

wynik = 0
for line in data:
    liczby = line.split(" ")
    M = int(liczby[0])
    a = int(liczby[1])
    b = int(liczby[2])

    zachodzi = False
    for x in range(0, M-1):
        if (a ** x % M) == b:
            zachodzi = True

    if zachodzi:
        wynik += 1

print(wynik)