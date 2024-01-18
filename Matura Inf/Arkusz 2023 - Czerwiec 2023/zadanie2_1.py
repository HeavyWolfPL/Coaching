def sufiks(slowo):
    slowo = str(slowo)
    temp = slowo
    lista = [slowo]
    for i in range(0, len(slowo)-1):
        temp = temp.replace(slowo[i], "", 1)
        lista.append(temp)
    return lista

def czy_mniejszy(s, k1, k2):
    n = len(s)
    x = 0 # DEBUG
    i = k1-1
    j = k2-1
    while i<=n and j<=n:
        if s[i] == s[j]:
            x += 1 # DEBUG
            i += 1
            j += 1
        else:
            x += 1
            if s[i] < s[j]:
                x += 1
                print(x)
                return True
            else:
                x += 1
                print(x)
                return False
    
    if j <= n:
        print(x)
        return True
    else:
        print(x)
        return False

wynik = sufiks("mascarpone")
print(wynik)
print(sorted(wynik))

print(czy_mniejszy("abababx", 1, 3))
# 6 porównań w pierszej instrukcji jeżeli, True
