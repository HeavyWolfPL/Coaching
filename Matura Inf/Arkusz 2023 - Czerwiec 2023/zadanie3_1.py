with open("DANE/przyklad.txt", mode="r") as file:
    dane = file.readlines()

zrownowazone = 0
prawie_zrown = 0

for line in dane:
    zera = 0
    jedyn = 0
    for i in range(0, len(line)):
        if line[i] == '0':
            zera += 1
        elif line[i] == '1':
            jedyn += 1

    if zera == jedyn:
        zrownowazone += 1
    elif (zera+1 == jedyn) or (jedyn+1 == zera):
        prawie_zrown += 1

print(zrownowazone)
print(prawie_zrown)