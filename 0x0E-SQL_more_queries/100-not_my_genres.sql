-- list all genres not linked to the show Dexter
SELECT DISTINCT
	g.name AS name
FROM
	tv_genres g
INNER JOIN
	tv_show_genres sg
ON
	s.id = sg.genre_id
WHERE
	sg.show_id != (SELECT id FROM tv_shows where title = "Dexter")
ORDER BY
	g.name;
