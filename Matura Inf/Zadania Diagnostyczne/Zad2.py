# Schemat kij wie kogo. 
# Dzielimy kwadrat naszej liczby n na wszystkie możliwe części. 
# Jeśli dana część zaczyna się od 0, np. 01 uznajemy to jako w tym przypadku 1.  
# Suma obu części (a+b) musi być mniejsza lub równa liczbie początkowej n, (a+b) <= n. 

# Zlicz ile występuje liczb w których występuje taki przypadek. Wypisz również liczby w którym są co najmniej dwie takie sumy.

with open(file="liczby2.txt", mode="r") as plik:
    dane = plik.readlines()

liczby = 0
liczby_dwa = 0
for n in dane:
    n = n.replace("\n", "")
    n = int(n)
    n2 = n**2
    n2 = str(n2)
    
    sumy = 0
    for index in range(1, len(n2)):
        a = n2[:index:]
        b = n2[index::]
        a, b = int(a), int(b)

        if a+b <= n:
            sumy += 1
    
    if sumy > 0:
        liczby += 1
        if sumy >= 2:
            liczby_dwa += 1

print(liczby, liczby_dwa)