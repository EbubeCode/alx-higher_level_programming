-- list all genres not linked to the show Dexter
SELECT DISTINCT
	title
FROM
	tv_shows s
LEFT JOIN
	tv_show_genres sg
ON
	s.id = sg.show_id
LEFT JOIN
(SELECT
	title
FROM
	tv_shows sh
INNER JOIN
	tv_show_genres sgen
ON
	sh.id = sgen.show_id
INNER JOIN
	tv_genres g
ON
	sgen.genre_id = g.id
WHERE g.name = "Comedy") c
USING (title)
WHERE
	c.title IS NULL
ORDER BY
	title;
