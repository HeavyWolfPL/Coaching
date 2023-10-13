plik = open("Dane_2305/pi.txt", "r")
dane = plik.readlines()

lista = []

for i in range(0, len(dane)-1):
    if i > (len(dane)-6):
        break
    liczba = dane[i][0] + dane[i+1][0] + dane[i+2][0] + dane[i+3][0] + dane[i+4][0] + dane[i+5][0]
    lista.append(liczba)

ciagi = []
for ciag in lista:
    # (00) i (0000)
    ciag = str(ciag)
    if (int(ciag[0]) < int(ciag[1])) and (int(ciag[2]) > int(ciag[3])) and (int(ciag[3]) > int(ciag[4])) and (int(ciag[4]) > int(ciag[5])): #(int(ciag[1]) >= int(ciag[2])) and (int(ciag[2]) > int(ciag[3])) and (int(ciag[3]) > int(ciag[4])) and (int(ciag[4]) > int(ciag[5])):
        ciagi.append(ciag)
    # (000) i (000)
    elif (int(ciag[0]) < int(ciag[1])) and (int(ciag[1]) < int(ciag[2])) and (int(ciag[3]) > int(ciag[4])) and (int(ciag[4]) > int(ciag[5])): #(int(ciag[2]) >= int(ciag[3])) and (int(ciag[3]) > int(ciag[4])) and (int(ciag[4]) > int(ciag[5])):
        ciagi.append(ciag)
    # (0000) i (00)
    elif (int(ciag[0]) < int(ciag[1])) and (int(ciag[1]) < int(ciag[2])) and (int(ciag[2]) < int(ciag[3])) and (int(ciag[4]) > int(ciag[5])): #(int(ciag[3]) >= int(ciag[4])) and (int(ciag[4]) > int(ciag[5])):
        ciagi.append(ciag)
    

wynik = len(ciagi)
print(wynik)

plik = open("wyniki3.txt", "a")
plik.write(f"3.3 {wynik}\n")