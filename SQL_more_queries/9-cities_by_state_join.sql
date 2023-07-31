-- Cities by States
SELECT cities.id, cities.name, states.name AS name FROM cities
JOIN states ON state_id = states.id ORDER BY cities.id ASC
