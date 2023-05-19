# Dane

# Funkcja
def Tura(k, A, B, s):
    i = s
    while i >= A[k]:
        if (B[i-A[k]] == 'P') and (B[i] == ''):
            B[i] = 'P'
        i -= 1

def Generator(poczatkowa, co_ile):
    A = []
    for i in range(0, 10):
        A.append(poczatkowa)
        poczatkowa *= co_ile
        if poczatkowa > 200:
            break
    
    dziala = True
    for s in range(1, 201):
        B = []
        for i in range(0, s+1):
            B.append('')

        n = s+1

        B[0] = 'P'
        for k in range(0, n):
            if len(A)-1 >= k:
                Tura(k, A, B, s)

        if B[s] != 'P':
            dziala = False
            break

    if dziala == True:
        return [True, A]
    else:
        return [False, A]


for i in range(1, 1000):
    for j in range(1, 100):
        wynik = Generator(i, j)
        if wynik[0] == True:
            print(i, j, wynik[1])

            

            

