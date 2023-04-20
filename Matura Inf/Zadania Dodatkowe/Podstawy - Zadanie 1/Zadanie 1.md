# Zadanie dodatkowe nr. 1
## Tablice i Operacje na plikach 

## Informacja
> Arkusz zawiera instrukcję w dwóch postaciach dla zadania. Treść zadania znajduje się w pliku PDF.

---

## Zadanie 1

### Warto wiedzieć
- [Tablice](../../Jak%20dziala%20X/Tablice/)
- [Operacje na plikach](../../Jak%20dziala%20X/Operacje%20na%20plikach/)

### Wytłumaczenie
> Standardowo odczytujemy sobie nasz plik początkowy.
> <br>Na sam początek warto by było zrobić sobie funkcje odpowiedzialne za przemianę DNA <> RNA. Jak i możemy opcjonalnie zrobić też funkcje które sprawdzą nam czy dana nić jest DNA lub RNA.

> Następnie dzielimy sobie nasze nici na DNA lub RNA zależnie od składu, do odpowiednich tablic. Wykorzystajmy wcześniej wspomniane funkcje do tego.
> <br>Po tym możemy już zrobić sobie naszą pierwszą część zadania, wypisanie nici do ich plików oraz statystykę. Funkcja len() będzie nam w tym pomocna.

> Nasze funkcje do przemiany nici DNA <> RNA warto zrobić za pomocą pętli i przemiany nici na listę, po czym jej połączenie w tekst. W ten sposób możemy łatwo przemienić każdą literę w nici.
> <br>Trzeba pamiętać że funkcja replace() nie pozwala na zamianę miejscami dwóch liter, dlatego warto to zrobić w pętli, lub wykorzystać literę tymczasową.

### Pseudo kod
```py
otwórz plik:
    przeczytaj zawartość

funkcja jest_DNA():
    sprawdź zawartość nici
funkcja jest_RNA():
    sprawdź zawartość nici

dla każdej linii w liniach pliku:
    jeśli linia jest DNA:
        dodaj do listy DNA

    jeśli linia jest RNA:
        dodaj do listy RNA

    wykonaj zapisy do plików


funkcja DNA_na_RNA():
    zamień nić na listę
    dla każdej litery w liście:
        jeśli litera jest X:
            zamień na Y
        jeśli litera jest Y:
            zamień na X

    połącz listę w tekst
    zwróć teksts

funkcja RNA_na_DNA():
    ### analogicznie jak wyżej


###  Powtórz dla każdego podpunktu
otwórz plik:
    zapisz do odpowiedniej zmiennej

dla każdej nici:
    użyj funkcji zamiany na odpowiednią nić

otwórz plik:
    zapisz wyniki do pliku
```

---

### Copyright 2023 - Wafelowski