-- join query
SELECT
	s.title AS title,
	g.genre_id AS genre_id
FROM
	tv_shows s
INNER JOIN
	tv_show_genres g
ON
	s.id = g.show_id
ORDER BY
	s.title,
	genre_id;
