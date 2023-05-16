-- A script to display a max temp of
-- each state
SELECT state, MAX (temperature)
AS max_temperature
FROM temperatures
GROUP BY state ORDER BY state;
