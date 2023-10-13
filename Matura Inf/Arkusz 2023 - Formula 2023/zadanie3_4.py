plik = open("Dane_2305/pi.txt", "r")
dane = plik.readlines()

lista = []



def funkcja(x):
    ciag = []
    pozycja = x+1
    # print(int(dane[x][0]), int(dane[x+1][0]))
    while int(dane[x][0]) < int(dane[x+1][0]):
        ciag.append(dane[x][0])
        x += 1

    if len(ciag) == 0:
        return

    while (int(dane[x][0]) >= int(dane[x+1][0])):
        if (int(dane[x-1][0]) == int(dane[x][0])) and (int(dane[x][0]) == int(dane[x+1][0])):
            break
        ciag.append(dane[x][0])
        x += 1
    
    if int(dane[x-1][0]) > int(dane[x][0]):
        ciag.append(dane[x][0])

    if len(ciag) < 4:
        return
    lista.append([pozycja, ciag])


i = 0 
while i < (len(dane)-4):
    funkcja(i)
    i += 1

najwiekszy = [0, []]
for ciag in lista:
    if len(ciag[1]) > len(najwiekszy[1]):
        najwiekszy = ciag


print(najwiekszy)

najwiekszy[1] = ''.join(najwiekszy[1])

plik = open("wyniki3.txt", "a")
plik.write(f"3.4 {najwiekszy[0]}, {najwiekszy[1]}\n")