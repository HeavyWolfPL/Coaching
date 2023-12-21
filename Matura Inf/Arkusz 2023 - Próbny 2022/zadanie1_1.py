with open("Dane/mecz_przyklad.txt", mode="r") as file:
    dane = file.readlines()
    dane = dane[0]

print(dane)
wygrane = 0
for i in range(1, len(dane)):
    if dane[i] != dane[i-1]:
        wygrane += 1

print(wygrane)