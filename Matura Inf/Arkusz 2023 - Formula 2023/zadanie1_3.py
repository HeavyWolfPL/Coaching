temp = []

# Nie działa, podaje inne odpowiedzi. Czyżby matura była błędna?



# def A(B, i, j):
#     temp.append(B[i][j])
#     # print(B[i][j])
#     if B[i+1][2*j-1] != '':
#         A(B, i+1, 2*j-1)
#     if B[i+1][2*j] != '':
#         A(B, i+1, 2*j)

def A(i, j, B):
    # Sprawdź, czy istnieje przegródka B[i, j]
    if B[i][j] != '':
        # Wypisz numer książki z przegródki B[i, j]
        print(B[i][j])
        temp.append(B[i][j])
        
        # Sprawdź, czy przegródka B[i + 1, 2j – 1] nie jest pusta
        if B[i+1][2*j-1] != '':
            A(i+1, 2*j-1, B)
        
        # Sprawdź, czy przegródka B[i + 1, 2j] nie jest pusta
        if B[i+1][2*j] != '':
            A(i+1, 2*j, B)

# Napisz funkcje:
# A(i, j) 
#   wypisz numer książki z przegródki B[i, j] 
#   jeżeli przegródka B[i + 1, 2j – 1] nie jest pusta, to  
#       wykonaj A(i + 1, 2j – 1) 
#   jeżeli przegródka B[i + 1, 2j] nie jest pusta, to  
#       wykonaj A(i + 1, 2j)




przyklad = [
    [10],
    [2, 15],
    [1, 5, 13, 25],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
]

biblioteczka = [
    [9], 
    [2, 12],
    ['', '', 10, 14],
    ['', '', '', '', '', '', 13, 15],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
]

biblioteczka2 = [
    [10], 
    [8, 15],
    [4, '', 12, ''],
    ['', 6, '', '', '', 13, '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
]

A(0, 0, biblioteczka)

print(f"Przykład: {temp}")

# temp = []
# print(f"Biblioteczka 1: {A(biblioteczka, 0, 0)}")

# temp = []
# print(f"Biblioteczka 2: {A(biblioteczka2, 0, 0)}")