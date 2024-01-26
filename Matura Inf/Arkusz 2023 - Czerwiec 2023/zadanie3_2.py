with open("DANE/anagram.txt", mode="r") as file:
    dane = file.readlines()

lista = []

for line in dane:
    zera = 0
    jedyn = 0
    line = line.replace("\n", "")
    for i in range(0, len(line)):
        if line[i] == '0':
            zera += 1
        elif line[i] == '1':
            jedyn += 1

    if zera == 4 and jedyn == 4:
        lista.append(line)
    elif zera == 3 and jedyn == 5:
        lista.append(line)
    # elif zera == 5 and jedyn == 3:
    #     lista.append(line)

print(lista)