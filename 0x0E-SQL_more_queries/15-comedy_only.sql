-- This script lists all Comedy shows in the database hbtn_0d_tv_shows

SELECT tv_shows.title AS title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE name = 'Comedy'
ORDER BY title;
