# Dane
s = 500
A = []

for i in range(5, 105, 5):
    A.append(i)

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

count = 0
for pole in B:
    if pole == 'P':
        count += 1

print(count)

