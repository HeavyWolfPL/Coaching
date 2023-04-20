# Operatory
##### Dowiesz się o wszystkich operatorach arytmetycznych, porównania, przypisania i logicznych. Operatory przynależności i identyczności istnieją tylko w Pythonie.


## Spis Treści
1. [Operatory Arytmetyczne](#operatory-arytmetyczne)
2. [Operatory Porównania](#operatory-porównania)
3. [Operatory Przypisania](#operatory-przypisania)
4. [Operatory Logiczne](#operatory-logiczne)
5. [Operatory Przynależności](#operatory-przynależnościowe)
6. [Operatory Identyczności](#operatory-identyfikacyjne)

---

## Operatory Arytmetyczne

#### Dodawania (+): Dodaje dwie zmienne do siebie
```py
a = 5
b = 3

x = "A"
y = "B"
print(a + b)  # Wynik: 8
print(x + y)  # Wynik: AB
```

#### Odejmowania (-): Odejmuje dwie zmienne od siebie
```py
a = 5
b = 3

x = "A"
y = "B"
print(a - b) # Wynik: 2
print(x - y) # Wynik: Błąd, nie można odejmować tekstu
```

#### Mnożenia (*): Mnoży dwie zmienne przez siebie
```py
a = 5
b = 3

x = "A"
y = "B"
print(a * b) # Wynik: 15
print(x * y) # Wynik: Błąd, nie można mnożyć tekstu przez tekst
print(x * b) # Wynik: AAA
```

#### Dzielenia (/): Dzieli jedną zmienną przez drugą
```py
a = 5
b = 3

x = "A"
y = "B"
print(a / b)  # Wynik: 1.6666666666666667
print(x / y)  # Wynik: Błąd, nie można dzielić tekstu przez tekst
```

#### Dzielenie z zaokrągleniem (//): Dzieli jedną zmienną przez drugą i zaokrągla wynik w dół
```py
a = 5
b = 3

print(a // b)  # Wynik: 1
```

#### Modulo (%): Zwraca resztę z dzielenia
```py
a = 5
b = 3
print(a % b)  # Wynik: 2
# Ponieważ 5 - 3 = 2
```

#### Potęga (**): 
```py
a = 5
b = 3
print(a ** b)  # Wynik: 125
```

## Operatory Porównania

#### Równe (==): Sprawdza czy dwie zmienne są równe
```py
a = 5
b = 5

x = "5"
print(a == b)  # Wynik: True
print(a == x)  # Wynik: False
```

#### Nie jest równe (!=): Sprawdza czy dwie zmienne nie są równe
```py
a = 5
b = 3

x = "5
print(a != b)  # Wynik: True
print(a != x)  # Wynik: True
```

#### Większe lub Mniejsze (> lub <): Sprawdza czy jedna zmienna jest większa od drugiej
```py
a = 5
b = 3

x = '4'
print(a > b)  # Wynik: True
print(a < b)  # Wynik: False
print(a > x)  # Wynik: Błąd, nie można porównywać liczb z tekstem
```

#### Większe/mniejsze lub równe (>= lub <=): Checks if one value is greater than or equal to another.
```py
a = 5
b = 3
c = 5

x = '5'
print(a >= b)  # Wynik: True
print(a <= b)  # Wynik: False
print(a >= c)  # Wynik: True
print(a <= c)  # Wynik: True
print(a >= x)  # Wynik: Błąd, nie można porównywać liczb z tekstem
```

## Operatory Przypisania

#### Przypisanie (=): Przypisuje wartość do zmiennej
```py
a = 5
b = "Tekst"
c = f"Tekst i zmienna a: {a}" # tzw. f-string
c = "Tekst i zmienna a: " + str(a) # Konwersja zmiennej a na tekst
c = "Tekst i zmienna a: {}".format(a) # Konwersja zmiennej a na tekst

print(a)  # Wynik: 5
print(b)  # Wynik: Tekst
print(c)  # Wynik: Tekst i zmienna a: 5
```

#### Przypisanie dodające (+=): Dodaje wartość do zmiennej i przypisuje wynik do zmiennej
```py
a = 5
a += 3

b = "Tekst"
b += " i dodatkowy tekst"

c = 5
c += "Tekst"
print(a)  # Wynik: 8
print(b)  # Wynik: Tekst i dodatkowy tekst
print(c)  # Wynik: Błąd, nie można dodawać tekstu do liczby
```

#### Przypisanie odejmujące (-=): Odejmuje wartość od zmiennej i przypisuje wynik do zmiennej
```py
a = 5
a -= 3

b = "Tekst"
b -= "ekst"
print(a)  # Wynik: 2
print(b)  # Wynik: Błąd, nie można odejmować tekstu od tekstu
```

#### Przypisanie z mnożeniem (*=): Mnoży wartość przez zmienną i przypisuje wynik do zmiennej
```py
a = 5
a *= 3

b = "Tekst"
b *= 3

c = "Tekst"
c *= "3"
print(a)  # Wynik: 15
print(b)  # Wynik: TekstTekstTekst
print(c)  # Wynik: Błąd, nie można mnożyć tekstu przez tekst
```

#### Przypisanie z mnożeniem (/=): Dzieli wartość przez zmienną i przypisuje wynik do zmiennej
```py
a = 15
a /= 3

b = "Tekst"
b /= 3

print(a)  # Wynik: 5.0
print(b)  # Wynik: Błąd, nie można dzielić tekstu przez liczbę
```

#### Przypisanie dzielenia z zaokrągleniem w dół (//=): Dzieli wartość przez zmienną i zaokrągla wynik w dół, a następnie przypisuje wynik do zmiennej
```py
a = 15
a //= 4

b = "Tekst"
b //= 3

print(a)  # Wynik: 3
print(b)  # Wynik: Błąd, nie można dzielić tekstu przez liczbę
```

#### Przypisanie z modulo (%=): Dzieli wartość przez zmienną i przypisuje resztę z dzielenia do zmiennej
```py
a = 15
a %= 4

b = "Tekst"
b %= 3

print(a)  # Wynik: 3
print(b)  # Wynik: Błąd, nie można dzielić tekstu przez liczbę
```

#### Przypisanie z potęgą (**=): Podnosi wartość do potęgi zmiennej i przypisuje wynik do zmiennej
```py
a = 5
a **= 3

b = "Tekst"
b **= 3

print(a)  # Wynik: 125
print(b)  # Wynik: Błąd, nie można potęgować tekstu
```

## Operatory Logiczne
> **operand** - argument(y) operatora
<br>

#### Operator I (and): Zwraca True jeśli oba operandy są True, False w przeciwnym wypadku
```py
a = 5 > 0 # True
b = 5 < 0 # False

c = 3
d = 6

print(a and b)  # Wynik: False
print(c and d)  # Wynik: 6
print(d and c)  # Wynik: 3
# Dlaczego? Nie wiem
```

#### Operator LUB (or): Zwraca True jeśli którykolwiek operand jest True, False w przeciwnym wypadku
```py
a = True
b = False

c = 3
d = 6

print(a and b)  # Wynik: False
print(c and d)  # Wynik: 3
print(d and c)  # Wynik: 6
```

#### Operator NIE JEST (not): Zwraca przeciwną wartość operandu
```py
a = True
b = False

c = 3 # True
d = 0 # False

print(not a)  # Wynik: False
print(not b)  # Wynik: True
print(not c)  # Wynik: False
print(not d)  # Wynik: True
```

## Operatory Przynależnościowe:

#### Przynależność (in): Zwraca True jeśli wartość jest znaleziona w sekwencji, False w przeciwnym wypadku
```py

a = [1, 2, 3, 4, 5]
b = 3

print(b in a)  # Wynik: True
print(6 in a)  # Wynik: False
```

#### Nieprzynależność (not in): Zwraca True jeśli wartość nie jest znaleziona w sekwencji, False w przeciwnym wypadku
```py
a = [1, 2, 3, 4, 5]
b = 3

print(b not in a)  # Wynik: False
print(6 not in a)  # Wynik: False
```

## Operatory Identyfikacyjne:
> W Pythonie "is" jest operatorem porównania referencji, podczas gdy "==" jest operatorem porównania wartości.
<br>Operator "is" porównuje, czy dwie zmienne wskazują na ten sam obiekt w pamięci. Oznacza to, że porównuje referencje do obiektów, nie zważając na ich rzeczywiste wartości.

> Wyobraź sobie przykład, w którym każda zmienna ma przydzielony dany unikalny numer. Jeśli przydzielisz dwóm zmiennym ten sam numer (np. a = c), to oznacza, że obie zmienne wskazują na ten sam obiekt w pamięci.
> Jeśli natomiast stworzysz dwie zmienne o tej samej wartości (np. a = 1, c = 1), to oznacza, że obie zmienne mają różne referencje, ale te same wartości.

#### Jest (is): Zwraca True jeśli obie zmienne wskazują na ten sam obiekt w pamięci, False w przeciwnym wypadku
```py
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False, ponieważ a i b wskazują na różne obiekty w pamięci
print(a is c)  # True, ponieważ a i c wskazują na ten sam obiekt w pamięci

print(a == b)  # True, ponieważ wartości obu zmiennych są takie same
print(a == c)  # True, ^
```

#### Nie jest (is not): Zwraca True jeśli obie zmienne nie wskazują na ten sam obiekt w pamięci, False w przeciwnym wypadku
```py
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is not b)  # True, ponieważ a i b wskazują na różne obiekty w pamięci
print(a is not c)  # False, ponieważ a i c wskazują na ten sam obiekt w pamięci

print(a != b)  # False, ponieważ a i b mają takie same wartości
print(a != c)  # False, ^
```

---

##### Copyright 2023 - Wafelowski