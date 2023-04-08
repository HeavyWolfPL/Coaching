# Arkusz Pokazowy - Matura Inf 2023

## Informacja
> Arkusz zawiera instrukcję w różnych postaciach dla każdego z zadań. Odpowiedzi oraz kod do każdego zadania znajdują się w plikach odpowiadających nazwom zadań.

## Spis Treści
1. [Zadanie 1.1](#zadanie-11)
2. [Zadanie 1.2](#zadanie-12)
3. [Zadanie 1.3](#zadanie-13)

---

## Zadanie 1.1

### Warto wiedzieć
- [Tablice](../../Jak%20dziala%20X/Tablice/)
- [Operacje na plikach](../../Jak%20dziala%20X/Operacje%20na%20plikach/)

### Wytłumaczenie
> Musimy sobie podzielić nasze partie szachowe na tablice. Każda partia to 8 linijek, zawierających 8 znaków. Do tego są one oddzielane pustą linią.
> <br>Na pierwszą myśl przychodzi dzielenie pliku po nowej linii, co jest już dobrym kierunkiem. Możemy liczyć do 8 i ignorować następną linię (która będzie pusta). Gdy policzymy do ośmiu, możemy poprzednie linie dodać do tablicy, którą dodamy do końcowej tablicy. W ten sposób będziemy mieli tablicę zawierającą wszystkie partie szachowe.

> Następnie musimy policzyć plansze z pustymi kolumnami oraz największa ilością pustych kolumn na planszy. Należy pamiętać że każda linia to wiersz, a nie kolumna, jak i że plansza może być pusta (!). 
> <br>W tym celu musimy przejść przez każdą kolumnę i wiersz by sprawdzić czy jest dana kolumna pusta. Jeśli jest pusta, to dodajemy 1 do zmiennej `pusteKolumny`. Na koniec sprawdzamy czy `pusteKolumny` jest większe od `maxPusteKolumny` i jeśli tak, to nadpisujemy `maxPusteKolumny` na `pusteKolumny`.
> <br>Wszystko oczywiście zapisujemy do pliku zgodnie z poleceniem.

### Pseudo kod
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

## Zadanie 1.2

### Warto wiedzieć
- [Tablice](../../Jak%20dziala%20X/Tablice/)
- [Operacje na plikach](../../Jak%20dziala%20X/Operacje%20na%20plikach/)

### Wytłumaczenie
> Część kodu sobie zabierzemy już z pierwszego zadania. Otrzymamy w ten sposób tablicę zawierającą partie szachowe, gdzie każda z nich sama w sobie jest tablicą zawierającą 8 linijek.

> Każdą z naszych plansz przekszałcimy sobie na tekst, by łatwiej było nam to później podzielić na wielkie i małe litery. Przy przekształcaniu usuniemy wszystkie zbędne nam znaki (nawiasy, przecinki, itd.). Następnie sprawdzimy każdą literę po kolei w pętli, i przydzielimy do odpowiedniej tablicy (małe lub wielkie). By porównać tablice należy pamiętać by były posortowane oraz tej samej wielkości, to osiągiemy na dwa sposoby:
>  - Przy dodawaniu litery do tablicy zmienimy jej wielkość
>  - W pętli zmienimy wielkość wszystkich liter w tablicy (Zamiana w tablicy używając indexu)

>  Następnie porównamy czy zawartość dwóch tablic jest identyczna. Jeśli tak, wykonujemy naszą statystykę dodając 1 do liczby plansz z równowagą. Jak i sprawdzając czy nasza liczba pionków jest mniejsza niż aktualna najmniejsza liczba pionków. Jeśli tak, to nadpisujemy ją na naszą.
> <br>Wszystko oczywiście zapisujemy do pliku zgodnie z poleceniem.

### Pseudo kod

```py
# tutaj dzielimy plansze

dla każdej planszy w liście plansz:
    zamień planszę na tekst + usuń zbędne znaki
    
    dla każdej litery w planszy:
        jeśli litera jest wielka:
            dodaj literę do tablicy wielkich
        jeśli litera jest mała:
            dodaj literę do tablicy małych

    dla każdej litery w tablicy wielkich:
        zamień literę na małą

    jeśli posortowana tablica wielkich jest równa posortowanej tablicy małych:
        planszeZRownowaga + 1
        jeśli liczba pionków jest mniejsza niż aktualna najmniejsza liczba pionków:
            najmniejszaLiczbaPionków = suma tablic
```

---

## Zadanie 1.3

### Warto wiedzieć
- [Tablice](../../Jak%20dziala%20X/Tablice/)
- [Operacje na plikach](../../Jak%20dziala%20X/Operacje%20na%20plikach/)

### Wytłumaczenie
> Część kodu sobie zabierzemy już z pierwszego zadania. Otrzymamy w ten sposób tablicę zawierającą partie szachowe, gdzie każda z nich sama w sobie jest tablicą zawierającą 8 linijek.

TODO: Wytłumaczenie
>  <br>Wszystko oczywiście zapisujemy do pliku zgodnie z poleceniem.

### Pseudo kod
> Poniższy pseudokod według mojej opinii jest dramatyczny, niezoptymalizowany i głupi. Jest lepszy sposób na to, poprawię go w najbliższym czasie.

```py
# tutaj dzielimy plansze

dla każdej planszy w liście plansz:
    zadeklaruj zmienne dla wybranych pionków

    dla każdej linii w planszy:
        dla każdego znaku w linii:
            jeśli znak jest równy literze pionka:
                ustaw zmienną pionka na koordynaty znaku

    jeśli król A oraz wieża B są na planszy:
        # (gdzie A oznacza jeden kolor, B oznacza drugi kolor)
        jeśli król A jest na tym samym wierszu co wieża B:
            zadeklaruj zmienną dla osi
        jeśli król A jest w tej samej kolumnie co wieża B:
            zadeklaruj zmienną dla osi

        jeśli oś nie jest zadeklarowana ORAZ istnieje druga wieża:
            jeśli król A jest na tym samym wierszu co druga wieża B:
                zadeklaruj zmienną dla osi
                zaznacz że używamy drugiej wieży
            jeśli król A jest w tej samej kolumnie co druga wieża B:
                zadeklaruj zmienną dla osi
                zaznacz że używamy drugiej wieży
        
        zadeklaruj zmienne dla zakresu liczbowego (od, do)
        jeśli oś jest równa X:
            jeśli używamy pierwszej wieży:
                zadeklaruj od jako minimalna liczba z dwóch
                zadeklaruj do jako maksymalna liczba z dwóch
            jeśli używamy drugiej wieży:
                zadeklaruj od jako minimalna liczba z dwóch
                zadeklaruj do jako maksymalna liczba z dwóch
        jeśli oś jest równa X:
            jeśli używamy pierwszej wieży:
                zadeklaruj od jako minimalna liczba z dwóch
                zadeklaruj do jako maksymalna liczba z dwóch
            jeśli używamy drugiej wieży:
                zadeklaruj od jako minimalna liczba z dwóch
                zadeklaruj do jako maksymalna liczba z dwóch

        
        jeśli zmienna od istnieje:
            zmienna pustej linii = True
            dla każdej linii w zakresie od do:
                jeśli linia nie pusta lub równa królowi:
                    zmienna pustej linii = False

            jeśli zmienna jest równa True:
                zmienna szacha dla koloru + 1

    jeśli król B oraz wieża A są na planszy:
        # Wykonujemy powyższy blok ale dla drugiej kombinacji kolorów
```

---

### Copyright 2023 - Wafelowski