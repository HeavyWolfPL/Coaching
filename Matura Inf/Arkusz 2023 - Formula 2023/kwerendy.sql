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