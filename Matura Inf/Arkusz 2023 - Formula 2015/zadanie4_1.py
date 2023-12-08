with open("Dane_2305/przyklad.txt", mode="r") as file:
    dane = file.readlines()

slowa_wk = []
for slowo in dane:
    litery = list(slowo)

    print(litery)

    litery_k = 0
    litery_w = 0

    for l in litery:
        if l == 'k':
            litery_k += 1
        elif l == 'w':
            litery_w += 1

    if litery_k == litery_w:
        slowa_wk.append(slowo)