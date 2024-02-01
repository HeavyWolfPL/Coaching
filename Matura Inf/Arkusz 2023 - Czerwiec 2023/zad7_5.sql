SELECT Firmy.nazwa, COUNT(Instalacje.id_firmy)
FROM Firmy INNER JOIN Instalacje ON Firmy.id_firmy = Instalacje.id_firmy
GROUP BY Firmy.nazwa
ORDER BY COUNT(Instalacje.id_firmy) DESC