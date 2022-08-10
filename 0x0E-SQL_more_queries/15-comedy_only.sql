-- join query with aggregation
SELECT
	s.title AS title
FROM
	tv_genres g
INNER JOIN
	tv_show_genres sg
ON
	g.id = sg.genre_id
INNER JOIN
	tv_shows s
ON
	sg.show_id = s.id
WHERE
	g.name = "Comedy"
ORDER BY
	s.title;
