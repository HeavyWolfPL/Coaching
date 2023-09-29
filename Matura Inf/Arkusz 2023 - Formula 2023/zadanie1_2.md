#### Treść zadania
Uzupełnij tabelkę – wpisz, ile minimalnie, a ile maksymalnie musi być półek w biblioteczce, żeby można było umieścić w niej n książek i żeby na ostatniej półce znalazła się co najmniej jedna książka. 

| n | min. | maks. |
| ------------- | ------------- | ------------- |
| 1 | 1 | 1 |
| 3 | 2 | 3 |
| 4 | 3 | 4 |
| 7 |   |   |
| 16 | 5 |   |
| 31 |   |   |
| 32 |   |   |
| 2<sup>k</sup>-1<br><sub>dla k > 0</sub> |   |   |

gdzie `n` jest liczbą książek, `min.` to minimalna liczba półek, a `maks.` to maksymalna liczba półek w biblioteczce.

#### Obliczenia
> Zakładając że:
> - i ≥ 0<br>
> - 1 ≤ j ≤ 2<sup>i</sup>

Jeśli `B[i, j]` jest:
- pusta → `B[i, j]`
- zajęta:
    - ma większy numer → `B[i + 1, 2j – 1]`
    - ma mniejszy numer → `B[i + 1, 2j]`

##### Założenia (może błędne)
- > min. = i + 1`
- > maks. = 2<sup>i</sup>
    - gdzie `i` jest liczbą półek w biblioteczce.

##### Matematyczny wzór
- > min. = log<sub>2</sub> x
    - `n` jest liczbą parzystą to `x = (n) + 1`
    - `n` jest liczbą nieparzystą to `x = (n + 1)`
- > maks. = 2<sup>log<sub>2</sub>(n)</sup>

**W przypadku 2<sup>k</sup>-1, dla k > 0** - nie wiem jak do tego doszło.

Wytłumaczenie filmowe - [link](https://youtu.be/LnJvb7Kb2yA?t=640). Chłop dał dupy z wytłumaczeniem tego wzoru.


#### Kod
```python
import math

def min_polki(n):
    if n % 2 == 0:
        return math.log2(n + 1)
    else:
        return math.log2(n + 1)
        
def maks_polki(n):
    return 2 ** math.log2(n)

print(min_polki(7))
# wynik: 3.0

print(maks_polki(7))
# wynik: 7.0
```