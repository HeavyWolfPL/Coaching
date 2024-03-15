# Plik liczby.txt zawiera liczby, które dzielimy na dwie części. 
# Liczba np. 3487 na pół to dwie liczby 34 i 87. 
# Największy wspólny dzielnik obu liczb to 1, nazywamy ją wtedy podzielnie pierwszą. 

# Wskaż ilość liczb podzielnie pierwszych w pliku. 

with open(file="liczby_przyklad.txt", mode="r") as plik:
    dane = plik.readlines()

def nwd(a, b):
    a = int(a)
    b = int(b)

    if b == 0:
        return a
    else:
        return nwd(b, a % b)
    
    # Drugi sposób:
    #
    # if a > b:
    #     max = a
    # else:
    #     max = b

    # najwiekszy = 0
    # for i in range(1, max):
    #     if a % i != 0 or b % i != 0:
    #         return najwiekszy
    #     else:
    #         najwiekszy = i

liczby = 0
for liczba in dane:
    liczba = liczba.replace("\n", "")
    index = len(liczba) // 2
    a = liczba[:index:]
    b = liczba[index::]
    
    # Drugi sposób:
    #
    # a, b = '', ''
    # for i in range(0, len(liczba)):
    #     if i <= (index // 2)+1:
    #         a = a + liczba[i]
    #     else:
    #         b = b + liczba[i]1
    print(a, b, liczba)

    podzielnie_pierwsz = nwd(a, b)
    if podzielnie_pierwsz == 1:
        liczby += 1

print(liczby)