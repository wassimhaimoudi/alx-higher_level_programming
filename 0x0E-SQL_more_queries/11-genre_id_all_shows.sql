-- This script lists all the shows contained in hbtn_0d_tvshows
-- If the show does not have a genre display NULL
SELECT ts.title, tg.genre_id 
FROM tv_shows AS ts 
LEFT JOIN tv_show_genres AS tg 
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id;
