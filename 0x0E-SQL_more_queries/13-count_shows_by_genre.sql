-- join query with aggregation
SELECT
	g.name AS genre,
	COUNT(*) as number_of_shows
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
GROUP BY
	g.name
ORDER BY
	number_of_shows DESC;
