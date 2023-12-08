with open("Dane_2305/przyklad.txt", mode="r") as file:
    dane = file.readlines()

slowa_wk = []
for slowo in dane:
    litery = list(slowo)

    l_w = 0
    l_a = 0
    l_k = 0
    l_c = 0
    l_j = 0
    l_e = 0
    ilosc_slow = 0

    for l in litery:
        if l == 'w':
            l_w += 1
        elif l == 'a':
            l_a += 1
        elif l == 'k':
            l_k += 1
        elif l == 'c':
            l_c += 1
        elif l == 'j':
            l_j += 1
        elif l == 'e':
            l_e += 1

    while l_w != 0:
        if (l_w >= 1) and (l_a >= 2) and (l_k >= 1) and (l_c >= 1) and (l_j >= 1) and (l_e >= 1):
            ilosc_slow += 1
            l_w -= 1
            l_a -= 2
            l_k -= 1
            l_c -= 1
            l_j -= 1
            l_e -= 1
        else:
            break

    print(ilosc_slow)