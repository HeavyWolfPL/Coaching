def sufiks(slowo):
    slowo = str(slowo)
    temp = slowo
    lista = [slowo]
    for i in range(0, len(slowo)-1):
        temp = temp.replace(slowo[i], "", 1)
        lista.append(temp)
    return lista

def czy_mniejszy(s, k1, k2):
    n = len(s)-1
    i = k1-1
    j = k2-1
    while i<=n and j<=n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return "TAK"
            else:
                return "NIE"
    
    if j <= n:
        return "TAK"
    else:
        return "NIE"
    
with open("DANE/slowa1.txt", mode="r") as file:
    slowa1 = file.readlines()

with open("DANE/slowa2.txt", mode="r") as file:
    slowa2 = file.readlines()

with open("DANE/slowa3.txt", mode="r") as file:
    slowa3 = file.readlines()

slowa1[1] = slowa1[1].replace("\n", "")
slowa1[2] = slowa1[2].replace("\n", "").split(" ")
slowa1 = czy_mniejszy(
        s = slowa1[1], 
        k1 = int(slowa1[2][0]), 
        k2 = int(slowa1[2][1])
    )

slowa2[1] = slowa2[1].replace("\n", "")
slowa2[2] = slowa2[2].replace("\n", "").split(" ")
slowa2 = czy_mniejszy(
        s = slowa2[1], 
        k1 = int(slowa2[2][0]), 
        k2 = int(slowa2[2][1])
    )

slowa3[1] = slowa3[1].replace("\n", "")
slowa3[2] = slowa3[2].replace("\n", "").split(" ")
slowa3 = czy_mniejszy(
        s = slowa3[1], 
        k1 = int(slowa3[2][0]), 
        k2 = int(slowa3[2][1])
    )

with open("wyniki2_2.txt", mode="w") as file:
    file.write(slowa1 + "\n")
    file.write(slowa2 + "\n")
    file.write(slowa3)