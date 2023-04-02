# Arkusz Pokazowy - Matura Inf 2023

### Informacja
Arkusz zawiera instrukcję w różnych postaciach dla każdego z zadań. Odpowiedzi oraz kod do każdego zadania znajdują się w plikach odpowiadających nazwom zadań.

---

### Zadanie 1.1

##### Warto wiedzieć
- [Tablice](../../Jak%20dziala%20X/Tablice/)
- [Operacje na plikach](../../Jak%20dziala%20X/Operacje%20na%20plikach/))

##### Wytłumaczenie
Musimy sobie podzielić nasze partie szachowe na tablice. Każda partia to 8 linijek, zawierających 8 znaków. Do tego są one oddzielane pustą linią.
<br>Na pierwszą myśl przychodzi dzielenie pliku po nowej linii, co jest już dobrym kierunkiem. Możemy liczyć do 8 i ignorować następną linię (która będzie pusta). Gdy policzymy do ośmiu, możemy poprzednie linie dodać do tablicy, którą dodamy do końcowej tablicy. W ten sposób będziemy mieli tablicę zawierającą wszystkie partie szachowe.
<br>

Następnie musimy policzyć plansze z pustymi kolumnami oraz największa ilością pustych kolumn na planszy. Należy pamiętać że każda linia to wiersz, a nie kolumna, jak i że plansza może być pusta (!). 
<br>W tym celu musimy przejść przez każdą kolumnę i wiersz by sprawdzić czy jest dana kolumna pusta. Jeśli jest pusta, to dodajemy 1 do zmiennej `pusteKolumny`. Na koniec sprawdzamy czy `pusteKolumny` jest większe od `maxPusteKolumny` i jeśli tak, to nadpisujemy `maxPusteKolumny` na `pusteKolumny`.

##### Pseudo kod
```py
otwórz plik
    przeczytaj zawartość
    zmienna i = 0
    zmienna plansza = []
    zmienna wszystkie_plansze = []
    dla każdej linii w pliku:
        jeśli i == 8:
            dodaj plansze do wszystkich plansz
            zmienna plansza = []
            zmienna i = 0
            pomiń linie
        i + 1
        dodaj linie do planszy
    dodaj planszę do plansz

dla każdej planszy w liście plansz:
    jeśli plansza jest pusta:
        pomiń
    zmienna pusteKolumny = 0
    dla każdej kolumny od 0 do 7:
        zmienna pusta = True
        dla każdego wiersza od 0 do 7:
            jeśli wiersz w kolumnie jest różny od kropki:
                pusta = False
                przerwij pętlę
        jeśli pusta:
            pusteKolumny + 1
    jeśli pusteKolumny != 0:
        pustePlansze + 1
    jeśli pusteKolumny > maxPusteKolumny:
        maxPusteKolumny = pusteKolumny
```

---

##### Copyright 2023 - Wafelowski