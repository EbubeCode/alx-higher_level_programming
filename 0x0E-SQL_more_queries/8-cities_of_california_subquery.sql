-- creates a nested query
SELECT
	id, name
FROM
	cities c
WHERE
	c.state_id = 
	(SELECT id FROM states s WHERE s.name = 'California')
ORDER BY
	id;
