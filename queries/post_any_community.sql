-- :name post_by_any_community :many
SELECT * FROM posts
ORDER BY PostDate
Limit :n;
