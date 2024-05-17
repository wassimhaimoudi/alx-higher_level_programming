-- This script dispalys the average temperature (Fahrenheit) by city ordered by the temperature(descending).
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
