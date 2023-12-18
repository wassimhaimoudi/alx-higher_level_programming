-- This script lists all cities in the database hbtn_0d_usa --
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM states INNER JOIN cities
WHERE states.id = cities.id
ORDER BY cities.id;
