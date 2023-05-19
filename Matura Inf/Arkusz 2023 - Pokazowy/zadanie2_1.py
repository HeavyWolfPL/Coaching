# Dane
s = 130
A = [1, 16, 31, 46, 61, 76, 91, 106, 121, 136]



B = []
for i in range(0, s+1):
    B.append('')

i = s
n = s+1

# Funkcja
def Tura(k):
    i = s
    while i >= A[k]:
        print(f"i = {i}, B[i-A[k] = {B[i-A[k]]}, B[i] = {B[i]}")
        if (B[i-A[k]] == 'P') and (B[i] == ''):
            B[i] = 'P'
        i -= 1

# Rozgrywka
B[0] = 'P'
for k in range(0, n):
    if len(A)-1 >= k:
        print(f"Tura - {k}, A = {A[k]}")
        Tura(k)

print(B)

if B[s] == 'P':
    print("Sukces!")
else:
    print("Nie ma sukcesu.")


