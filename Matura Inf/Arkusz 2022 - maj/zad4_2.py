with open(file="Dane_2205/liczby.txt", mode="r") as plik:
    dane = plik.readlines()


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def genPrimes(max):
    primes = []
    for i in range(2, (max//2)+1):
        if is_prime(i):
            primes.append(i)
    return primes

liczby = 0
maks_czynnikow = [0, 0]
maks_roznych = [0, 0]
for liczba in dane:
    liczba = liczba.replace("\n", "")
    liczba = int(liczba)

    if is_prime(liczba):
        pierwsze = [liczba]
    else:
        pierwsze = genPrimes(liczba)
        pierwsze = sorted(pierwsze, reverse=True)

    liczba_tym = liczba
    czynniki = []
    while liczba_tym != 1:
        for i in pierwsze:
            if (liczba_tym % i) == 0:
                czynniki.append(i)
                liczba_tym = (liczba_tym // i)
                break

    czynniki_rozn = []
    for i in czynniki:
        if i not in czynniki_rozn:
            czynniki_rozn.append(i)

    if len(czynniki) > maks_czynnikow[1]:
        maks_czynnikow = [liczba, len(czynniki)]

    if len(czynniki_rozn) > maks_roznych[1]:
        maks_roznych = [liczba, len(czynniki_rozn)]

    # print(liczba, liczba_tym, czynniki, czynniki_rozn, pierwsze)

print(maks_czynnikow[0], maks_czynnikow[1], maks_roznych[0], maks_roznych[1])
