-- :name n_post_by_time :many
SELECT * FROM posts
ORDER BY PostDate
Limit :n;
