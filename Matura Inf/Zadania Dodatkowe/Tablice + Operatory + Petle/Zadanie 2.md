# Zadanie dodatkowe nr. 2
## Tablice, Operacje na plikach i Pętle

## Informacja
> Arkusz zawiera instrukcję w dwóch postaciach dla zadania. Treść zadania znajdziesz poniżej.

---

## Zadanie 1

### Polecenie
> Projektujesz generator kodów liczbowych.
> Generator tworzy liczby czterocyfrowe, niepowtarzalne i wykorzystujący daną cyfrę `0 - 9` dokładnie raz.
> <br>Generator działa według zasady:
> <br>`0 -> 9`, 
> <br>`1 -> 0`, 
> <br>`1 -> 2`, 
> <br>`1 -> 6`, 
> <br>`2 -> 3`, 
> <br>`3 -> 5`, 
> <br>`3 -> 4`, 
> <br>`6 -> 5`, 
> <br>`5 -> 7`, 
> <br>`7 -> 8`, 
> <br>`9 -> 7`
> <br>gdzie zapis:  `a -> b`  oznacza, że w zapisie generowanej liczby, cyfra a może wystąpić na lewo od cyfry b tylko w takich kombinacjach, jako jej sąsiad.
> 
> **Ale wpierw.** Ile liczb może zostać stworzonych?


### Warto wiedzieć
- [Tablice](../../Jak%20dziala%20X/Tablice/)
- [Operacje na plikach](../../Jak%20dziala%20X/Operacje%20na%20plikach/)
- Pętle (WIP)
- [Metoda zfill()](https://www.w3schools.com/python/ref_string_zfill.asp)

### Wytłumaczenie
> Stwórzmy sobie funkcję `generate()`, którą wywołamy później. Funkcja ta będzie generować wszystkie możliwe kombinacje liczb zgodnie z zasadą.
> <br>W funkcji zadeklarujmy sobie nasze wszystkie możliwe pary cyfr, które mogą wystąpić w liczbie.
> Następnie zrobimy pętle dla liczb maksymalnie czterocyfrowych, gdzie te krótsze wypełnimy zerami na początku.
> W pętli sprawdzimy sobie czy pary w liczbie spełniają zasady.

### Pseudo kod
```py
funkcja generate():
    zmienna liczby
    zmienna pary
    dla i od 1 do 9999:
        zamień i na tekst
        jeśli długość tekstu jest mniejsza od 4:
            użyj metody zfill()
        
        jeśli pary spełniają zasady:
            dodaj do listy liczby

wypisz liczby
wypisz długość listy liczby
```

---

### Copyright 2023 - Wafelowski