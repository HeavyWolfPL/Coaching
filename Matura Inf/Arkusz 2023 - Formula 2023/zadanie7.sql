
-- Zadanie 7.1
SELECT `nazwa`, COUNT(`oceny`.`id_gry`) AS 'Ilosc ocen' FROM `gry` 
INNER JOIN `oceny` ON `gry`.`id_gry` = `oceny`.`id_gry`
GROUP BY `gry`.`nazwa`  
ORDER BY `Ilosc ocen` DESC
LIMIT 1;


-- Zadanie 7.2
SELECT `nazwa`, ROUND(AVG(`oceny`.`ocena`), 2) AS 'Srednia ocen' FROM `gry` 
INNER JOIN `oceny` ON `gry`.`id_gry` = `oceny`.`id_gry`
WHERE `gry`.`kategoria` = 'imprezowa'
GROUP BY `gry`.`nazwa`;


-- Zadanie 7.3
-- główna kwerenda, połączona z poniższą
SELECT gracze.id_gracza, oceny_posiadaja.id_gracza
FROM (gracze LEFT JOIN oceny_posiadaja ON gracze.id_gracza = oceny_posiadaja.id_gracza) 
INNER JOIN oceny ON gracze.id_gracza = oceny.id_gracza
GROUP BY gracze.id_gracza, oceny_posiadaja.id_gracza
HAVING (((oceny_posiadaja.id_gracza) Is Null));

-- gracze posiadający jakąkolwiek grę
SELECT oceny.id_gracza, oceny.stan
FROM gry INNER JOIN (gracze INNER JOIN oceny ON gracze.id_gracza = oceny.id_gracza) ON gry.id_gry = oceny.id_gry
GROUP BY oceny.id_gracza, oceny.stan
HAVING (((oceny.stan)="posiada"));

-- ilość graczy nie posiadający żadnej gry
-- tego używamy tylko po to by odjąć od finalnej wersji
-- Zbędne, bo powyższe dwie już tak czy siak podają poprawny wynik
SELECT Count(gracze.id_gracza) AS PoliczOfid_gracza, oceny.id_gracza
FROM gracze LEFT JOIN oceny ON gracze.id_gracza = oceny.id_gracza
GROUP BY oceny.id_gracza
HAVING (((oceny.id_gracza) Is Null));


-- Zadanie 7.4
SELECT gry.nazwa, oceny.id_gry, COUNT(oceny.id_gry) AS 'Ilosc ocen' FROM `oceny`
INNER JOIN gracze ON oceny.id_gracza = gracze.id_gracza
INNER JOIN gry ON oceny.id_gry = gry.id_gry
WHERE gracze.wiek <= 19
GROUP BY oceny.id_gry
ORDER BY COUNT(oceny.id_gry) DESC
LIMIT 2;

SELECT gry.nazwa, oceny.id_gry, COUNT(oceny.id_gry) AS 'Ilosc ocen' FROM `oceny`
INNER JOIN gracze ON oceny.id_gracza = gracze.id_gracza
INNER JOIN gry ON oceny.id_gry = gry.id_gry
WHERE (gracze.wiek <= 49 AND gracze.wiek >= 20)
GROUP BY oceny.id_gry
ORDER BY COUNT(oceny.id_gry) DESC
LIMIT 1;

SELECT gry.nazwa, oceny.id_gry, COUNT(oceny.id_gry) AS 'Ilosc ocen' FROM `oceny`
INNER JOIN gracze ON oceny.id_gracza = gracze.id_gracza
INNER JOIN gry ON oceny.id_gry = gry.id_gry
WHERE gracze.wiek >= 50
GROUP BY oceny.id_gry
ORDER BY COUNT(oceny.id_gry) DESC
LIMIT 1;



-- Zadanie 7.5

SELECT SUM(sklep.cena) FROM sklep
INNER JOIN gry ON sklep.id_gry = gry.id_gry
WHERE ((gry.kategoria = 'logiczna') AND (sklep.promocja = 'true'));