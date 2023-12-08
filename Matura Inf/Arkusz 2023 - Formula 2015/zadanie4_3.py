with open("Dane_2305/przyklad.txt", mode="r") as file:
    dane = file.readlines()

    for linijka in dane:
        linijka = linijka.strip() # Usuwamy spacje
        ile_usunac = 0
        x_index = 0
        for litery in linijka:
            # Na każdą literę w słowie, sprawdź czy odpowiada temu samemu miejscu co w słowie wakacje.
            if litery == "wakacje"[x_index]:
                x_index += 1
                if x_index > 6:
                    x_index=0 # Wróć do pierwszej litery słowa wakacje
            else: # Nie odpowiada
                ile_usunac += 1
        print(ile_usunac + x_index, end=" ")