-- list all genres not linked to the show Dexter
SELECT DISTINCT
	name
FROM
	tv_genres g
INNER JOIN
	tv_show_genres sg
ON
	g.id = sg.genre_id
LEFT JOIN
(SELECT
	name
FROM
	tv_genres gen
INNER JOIN
	tv_show_genres sgen
ON
	gen.id = sgen.genre_id
INNER JOIN
	tv_shows s
ON
	sgen.show_id = s.id
WHERE s.title = "Dexter") d
USING (name)
WHERE
	d.name IS NULL
ORDER BY
	name;
