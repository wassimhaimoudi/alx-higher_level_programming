-- This script lists all records having a name of the table second_table of the database hbtn_0c_0 in descending order --
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
