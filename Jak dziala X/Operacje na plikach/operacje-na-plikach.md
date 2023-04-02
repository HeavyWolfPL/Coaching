# Operacje na plikach
##### Dowiesz się tutaj na jakiej zasadzie możemy pracować z plikami w Pythonie.

#### Zawartość pliku `przyklad.txt`
```txt
Lorem ipsum dolor sit amet.
Aut eveniet quas veritatis asperiores.
Repudiandae optio omnis blanditiis. Aliquid.
```

---

### Otwieranie pliku

```py
plik = open(file="przyklad.txt", mode="r") 
# W nastepnych linijkach wykonujemy operacje na pliku
plik.close() # Zamykamy plik by usunąć go z pamięci, nie jest to obowiązkowe
```

lub

```py
with open(file="przyklad.txt", mode="r") as plik:
    pass # Tutaj możemy wykonywać operacje na pliku
    # Po wyjściu z bloku with plik zostanie automatycznie zamknięty
```

#### Parametry
- **file** - nazwa pliku, nie musimy podawać przedrostku "file=" jeśli jest to pierwszy parametr
- **mode** - tryb otwarcia pliku, domyślnie "r" (read) czyli odczyt, wyróżniamy również:
    - "w" (write) czyli zapis, jeśli plik istnieje to zostanie nadpisany
    - "a" (append) czyli dopisanie do pliku, jeśli plik nie istnieje to zostanie utworzony
    - "x" (create) czyli utworzenie pliku, jeśli plik istnieje to zostanie wygenerowany błąd
    - "r+" czyli odczyt i zapis, jeśli plik nie istnieje to zostanie wygenerowany błąd
    - "w+" czyli odczyt i zapis, jeśli plik istnieje to zostanie nadpisany
    - "a+" czyli odczyt i dopisanie do pliku, jeśli plik nie istnieje to zostanie utworzony
    - "x+" czyli odczyt i utworzenie pliku, jeśli plik istnieje to zostanie wygenerowany błąd
- **encoding** - kodowanie pliku, domyślnie "utf-8"

---

### Odczyt zawartości

```py
plik = open(file="przyklad.txt", mode="r")
```

#### Uwaga!
Po odczytaniu pliku raz przy użyciu jednej z poniższych metod, nie będzie można go ponownie odczytać bez ponownego otwarcia pliku (workaround)
<br>Poprawnym sposobem było by przesunięcie kursora w pliku na sam początek, ale nie ma sensu tego pamiętać na maturze.

#### Odczyt całego pliku
```py
zawartosc = plik.read() # Zwraca stringa z zawartością pliku
```
```py
'Lorem ipsum dolor sit amet.\nAut eveniet quas veritatis asperiores.\nRepudiandae optio omnis blanditiis. Aliquid.\n'
```

#### Odczyt jednej linii
```py
zawartosc = plik.readline() # Zwraca stringa z zawartością linii, jako parametr przyjmuje liczbę znaków do odczytania
```
```py
'Lorem ipsum dolor sit amet.\n'
```

#### Odczyt wszystkich linii
```py
zawartosc = plik.readlines() # Zwraca listę (tablicę) stringów z zawartością linii
```
```py
['Lorem ipsum dolor sit amet.\n', 'Aut eveniet quas veritatis asperiores.\n', 'Repudiandae optio omnis blanditiis. Aliquid.\n']
```

#### Odczyt wszystkich linii (z użyciem pętli)
```py
zawartosc = []
for linia in plik:
    zawartosc.append(linia)
```
```py
['Lorem ipsum dolor sit amet.\n', 'Aut eveniet quas veritatis asperiores.\n', 'Repudiandae optio omnis blanditiis. Aliquid.\n']
```

---

### Zapis do pliku

```py
plik = open(file="przyklad.txt", mode="w")
```

#### Zapisanie stringa
```py
plik.write("Lorem ipsum dolor sit amet.")
```
```py
# Treść pliku:
Lorem ipsum dolor sit amet.
```

#### Zapisanie listy
```py
plik.writelines(["Lorem ipsum dolor sit amet.\n", "Aut eveniet quas veritatis asperiores.\n", "Repudiandae optio omnis blanditiis. Aliquid.\n"]) 
```
```py
# Treść pliku:
Lorem ipsum dolor sit amet.
Aut eveniet quas veritatis asperiores.
Repudiandae optio omnis blanditiis. Aliquid.
```

---

### Przykład
```py
with open(file="przyklad.txt", mode="a") as plik:
    plik.write("Lorem ipsum dolor sit amet.\n")
    plik.write("Aut eveniet quas veritatis asperiores.\n")

with open(file="przyklad.txt", mode="r") as plik:
    print(plik.read())

with open(file="przyklad.txt", mode="w") as plik:
    plik.write("Repudiandae optio omnis blanditiis. Aliquid.\n")

with open(file="przyklad.txt", mode="r") as plik:
    print(plik.read())
```

```py
Lorem ipsum dolor sit amet.
Aut eveniet quas veritatis asperiores.

Repudiandae optio omnis blanditiis. Aliquid.
```

---

##### Copyright 2023 - Wafelowski