-- this script lists all the cities of california that can be found in the database htbtn_0d_usa --
SELECT id, name 
FROM cities
WHERE state_id = (SELECT states.id FROM states WHERE name = 'California')
ORDER BY cities.id;
