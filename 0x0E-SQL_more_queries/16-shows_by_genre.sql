-- join query with aggregation
SELECT
	s.title AS title,
	g.name AS name
FROM
	tv_genres g
INNER JOIN
	tv_show_genres sg
ON
	g.id = sg.genre_id
RIGHT OUTER JOIN
	tv_shows s
ON
	sg.show_id = s.id
ORDER BY
	s.title, g.name;
