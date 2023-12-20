-- Lista todas las ciudades contenidas en la base de datos hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
