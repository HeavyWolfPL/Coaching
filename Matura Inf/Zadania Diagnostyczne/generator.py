import random

def nwd(a, b):
  while b:
    a, b = b, a % b
  return a

def generuj_liczbe():
  dlugosc = random.randint(4, 8)
  while dlugosc % 2 != 0:
    dlugosc += 1
    
  pierwsza_czesć = random.randint(10, 99)
  druga_czesć = random.randint(10, 99)
  liczba = pierwsza_czesć * 10 + druga_czesć
  while len(str(liczba)) != dlugosc:
    liczba = str(liczba) + str(random.randint(0, 9))
    liczba = int(liczba)
    
  return liczba

def main():
  liczba_liczb = int(input("Podaj liczbę liczb do wygenerowania: "))
  nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
  
  liczby_podzielnie_pierwsze = []
  while len(liczby_podzielnie_pierwsze) != liczba_liczb:
    liczba = generuj_liczbe()
    # Używamy wartości bezpośrednio z funkcji generującej
    if nwd(liczba // 10, liczba % 10) == 1:
      liczby_podzielnie_pierwsze.append(liczba)
  
  with open(nazwa_pliku, "w") as plik:
    for liczba in liczby_podzielnie_pierwsze:
      plik.write(f"{liczba}\n")

if __name__ == "__main__":
  main()