SELECT TOP 10 Pojemnosc_dysku, COUNT(Pojemnosc_dysku) AS 'Ilosc pojemnosci'
FROM komputery
GROUP BY Pojemnosc_dysku
ORDER BY COUNT(Pojemnosc_dysku) DESC;


-- Pojemnosc_dysku, COUNT(Pojemnosc_dysku)
-- 700              5


SELECT komputery.Numer_komputera, COUNT(awarie.Numer_komputera) AS ['IloscNapraw']
FROM (komputery INNER JOIN awarie ON komputery.Numer_komputera = awarie.Numer_komputera) INNER JOIN naprawy ON awarie.Numer_zgloszenia = naprawy.Numer_zgloszenia
WHERE (naprawy.rodzaj = 'wymiana' AND komputery.Sekcja = 'A')
GROUP BY komputery.Numer_komputera
HAVING COUNT(awarie.Numer_komputera) >= 10;


SELECT Count(Numer_komputera) AS ['Ilosc komputery']
FROM 3a;

SELECT komputery.Numer_komputera
FROM komputery LEFT JOIN awarie ON komputery.Numer_komputera = awarie.Numer_komputera
WHERE awarie.Numer_komputera IS NULL OR (awarie.Priorytet IS NULL OR awarie.Priorytet < 8)
GROUP BY komputery.Numer_komputera;
