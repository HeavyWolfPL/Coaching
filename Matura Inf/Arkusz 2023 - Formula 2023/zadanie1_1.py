ksiazki = [14, 18, 12, 9, 20, 15, 17]

i = 4 # Półki
B = []

for polka in range(0, i+1):
    przegrody = []
    for przegroda in range(0, 2**polka):
        przegrody.append('')

    B.append(przegrody)

i = 0
j = 0
B[0][0] = ksiazki[0]
ksiazki.pop(0)
for polka, przegrody in enumerate(B):
    print(polka, przegrody, len(przegrody))
print()

for ksiazka in ksiazki:
    i = 0
    j = 0
    while True:
        if B[i][j] == '':
            break
        elif B[i][j] > ksiazka:
            i += 1
            j += 1
            j = (2 * j) - 2
        elif B[i][j] < ksiazka:
            i += 1
            j += 1
            j = (2*j) - 1
    B[i][j] = ksiazka



for polka, przegrody in enumerate(B):
    print(polka, przegrody, len(przegrody))

