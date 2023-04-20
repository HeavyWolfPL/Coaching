# Wszystkie możliwe pary:
# [0, 9], [1, 0], [1, 2], [1, 6], [2, 3], [3, 4], [3, 5], [5, 7], [6, 5], [7, 8], [9, 7]
# ["09", "10", "12", "16", "23", "34", "35", "57", "65", "78", "97"]

def generate():
    codes = []
    pairs = ["09", "10", "12", "16", "23", "34", "35", "57", "65", "78", "97"] # Tworzymy sobie listę wszystkich par
    for i in range(1, 9999): # Na zakres czterocyfrowy
        i = str(i) # Ułatwi nam to życie, gdyż nie można brać danego indexu z liczby
        if len(i) < 4: # Jeśli liczba nie posiada 4 cyfr
            i = i.zfill(4) # Uzupełnij ją zerami, posłuży nam do tego metoda .zfill()
            # https://www.w3schools.com/python/ref_string_zfill.asp
        
        # Tutaj sprawdzimy czy liczba spełnia warunki w obu parach
        if (i[0] + i[1] in pairs) and (i[1] + i[2] in pairs)and (i[2] + i[3] in pairs):
            if i not in codes: # Jeśli liczba już nie występuje
                codes.append(i) # Dodaj do tablicy

    # codes = sorted(codes) # Możemy sobie posortować jak ktoś lubi
    print(codes)

generate()