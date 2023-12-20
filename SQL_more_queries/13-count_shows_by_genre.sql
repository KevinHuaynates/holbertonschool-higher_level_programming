-- 13. Number of shows by genre: Lista todos los géneros de hbtn_0d_tvshows y muestra el número de programas vinculados a cada uno.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;

