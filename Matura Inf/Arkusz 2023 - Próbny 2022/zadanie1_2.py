with open("Dane/mecz_przyklad.txt", mode="r") as file:
    dane = file.readlines()
    dane = dane[0]

A = 0
B = 0
wygral = ""
for i in range(0, len(dane)):
    if dane[i] == "A":
        A += 1
    elif dane[i] == "B":
        B += 1

    if (A >= 1000) and (A-B >= 3):
        wygral = "A"
        break
    elif (B >= 1000) and (B-A >= 3):
        wygral = "B"
        break

print(f"{wygral} {A}:{B}")