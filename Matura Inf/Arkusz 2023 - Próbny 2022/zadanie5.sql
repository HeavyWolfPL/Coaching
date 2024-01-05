
-- 5.1
SELECT Klienci.imie, Klienci.nazwisko, SUM(DateDiff('d',[data_przyjazdu],[data_wyjazdu])) AS Suma_dni
FROM Noclegi INNER JOIN Klienci ON Noclegi.nr_dowodu = Klienci.nr_dowodu
GROUP BY Klienci.nazwisko, Klienci.imie, Noclegi.nr_dowodu
ORDER BY SUM(DateDiff('d',[data_przyjazdu],[data_wyjazdu])) DESC;

-- 5.2
SELECT zad2a.imie, zad2a.nazwisko, SUM(zad2a.Kwota)
FROM zad2a
GROUP BY zad2a.imie, zad2a.nazwisko
HAVING SUM(zad2a.Kwota) > 2000
ORDER BY SUM(zad2a.Kwota) DESC;

-- dodatkowe
SELECT Klienci.imie, Klienci.nazwisko, Noclegi.nr_pokoju, Pokoje.cena, DateDiff('d',[data_przyjazdu],[data_wyjazdu]) AS Dni, Pokoje.cena * Dni AS Kwota
FROM (Noclegi INNER JOIN Klienci ON Noclegi.nr_dowodu = Klienci.nr_dowodu) INNER JOIN Pokoje ON Noclegi.nr_pokoju = Pokoje.nr_pokoju
GROUP BY Klienci.nazwisko, Klienci.imie, Noclegi.nr_dowodu, Noclegi.nr_pokoju, Pokoje.cena, DateDiff('d',[data_przyjazdu],[data_wyjazdu]);


-- 5.3
SELECT Pokoje.nr_pokoju
FROM Pokoje
WHERE (Pokoje.nr_pokoju NOT IN (SELECT * from zad3a)) AND (Pokoje.standard = 'N')

-- dodatkowe
SELECT Pokoje.nr_pokoju
FROM (Pokoje INNER JOIN Noclegi ON Pokoje.nr_pokoju = Noclegi.nr_pokoju) INNER JOIN Klienci ON Klienci.nr_dowodu = Noclegi.nr_dowodu
WHERE ((Pokoje.standard = 'N') AND (Noclegi.data_przyjazdu BETWEEN #2022-07-01# AND #2022-09-30#) AND (Klienci.miejscowosc IN ('Opole', 'Katowice')))
GROUP BY Pokoje.nr_pokoju;


-- 5.4
SELECT uslugi_dodatkowe.rodzaj, COUNT(*)
FROM uslugi_dodatkowe
GROUP BY uslugi_dodatkowe.rodzaj

-- 5.5
SELECT Klienci.imie, Klienci.nazwisko, SUM(uslugi_dodatkowe.cena_uslugi)
FROM (Klienci INNER JOIN Noclegi ON Klienci.nr_dowodu = Noclegi.nr_dowodu) INNER JOIN uslugi_dodatkowe ON Noclegi.id_pobytu = uslugi_dodatkowe.id_pobytu
GROUP BY Klienci.imie, Klienci.nazwisko, SUM(uslugi_dodatkowe.cena_uslugi)