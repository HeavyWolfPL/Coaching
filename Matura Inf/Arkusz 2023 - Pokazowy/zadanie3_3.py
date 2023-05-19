with open("zalaczniki/liczby_przyklad.txt", mode="r") as file:
    data = file.readlines()


wynik = 0
for line in data:
    liczby = line.split(" ")
    print(liczby)

    dzieli = False
    liczby[0] = int(liczby[0])
    for i in range(2, liczby[0]):
        if liczby[0] % i == 0:
            dzieli = True
        
    if dzieli == False:
        wynik += 1

print(wynik)