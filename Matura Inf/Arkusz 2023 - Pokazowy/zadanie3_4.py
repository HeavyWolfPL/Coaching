with open("zalaczniki/liczby_przyklad.txt", mode="r") as file:
    data = file.readlines()

def NWD(liczby):
    dzielniki = []

    for x in liczby:
        dzielLiczby = []
        for i in range(1, x+1):
            if x % i == 0:
                dzielLiczby.append(i)

        dzielniki.append(dzielLiczby)

    nwd = 1
    for x in dzielniki[0]:
        if x in dzielniki[1]:
            if x > nwd:
                nwd = x

    if nwd == 1:
        print(dzielniki[0], dzielniki[1])
        return True
    else:
        return False
 
wynik = 0
for line in data:
    liczba = line.split(" ")
    a = int(liczba[0])
    b = int(liczba[1])
     
    if NWD([a, b]):
        wynik += 1
    

print(wynik)