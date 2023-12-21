with open("Dane/mecz_przyklad.txt", mode="r") as file:
    dane = file.readlines()
    dane = dane[0]

najdluzsza = [0, ""]
lacznie = 0

dane = dane.replace("AB", "AXB")
dane = dane.replace("BA", "BXA")
dane = dane.split("X")

for x in dane:
    if len(x) >= 10:
        lacznie += 1
        if len(x) > najdluzsza[0]:
            najdluzsza[0] = len(x)
            najdluzsza[1] = x[0]

print(f"{lacznie} {najdluzsza[1]} {najdluzsza[0]}")