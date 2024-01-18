def sufiks(slowo):
    slowo = str(slowo)
    temp = slowo
    lista = [slowo]
    for i in range(0, len(slowo)-1):
        temp = temp.replace(slowo[i], "", 1)
        lista.append(temp)
    return lista
    
# def sortowanie_babelkowe(slowa):
#     n = len(slowa)

#     for i in range(0, n-1):
#         for j in range(0, n-i-1):
#             if slowa[j] > slowa[j+1]:
#                 slowa[j], slowa[j+1] = slowa[j+1], slowa[j]

#     return slowa

wyniki = []
with open("DANE/slowa4.txt", mode="r") as file:
    dane = file.readlines()

for slowo in dane:
    slowo = slowo.split(" ")[1].replace("\n", "")
    print(slowo)

    wyniki.append(sorted(sufiks(slowo))[0])

with open("wyniki2_4.txt", mode="w") as file:
    for x in wyniki:
        file.write(x + "\n")