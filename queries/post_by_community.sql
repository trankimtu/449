-- :name post_by_community :many
SELECT * FROM posts
WHERE Community = :Community
ORDER BY PostDate
Limit :n;



