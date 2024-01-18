def sufiks(slowo):
    slowo = str(slowo)
    temp = slowo
    lista = [[1, slowo]]
    for i in range(0, len(slowo)-1):
        temp = temp.replace(slowo[i], "", 1)
        lista.append([i+2, temp])
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
    
def sortowanie_babelkowe(slowa):
    n = len(slowa)

    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if slowa[j][1] > slowa[j+1][1]:
                slowa[j], slowa[j+1] = slowa[j+1], slowa[j]
                # a, b = b, a --> a = b, b = a

    return slowa

lista = sufiks("mascarpone")
print(lista)
print(sortowanie_babelkowe(lista))

indexy = []
for i in sortowanie_babelkowe(lista):
    indexy.append(i[0])

print(indexy)