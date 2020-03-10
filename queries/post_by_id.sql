-- :name post_by_id :one
SELECT * FROM posts
WHERE PostID = :PostID;
