with open("Dane_2212/liczby_przyklad.txt", mode="r") as file:
    dane = file.readlines()

pierwsze = []

for i in dane:
    i = int(i)-1
    pierwsza = True
    for j in range(2, i):
        if i % j == 0:
            pierwsza = False
            break
    
    if pierwsza:
        pierwsze.append(i+1)

print(len(pierwsze))