-- :name vote_by_postid :one
SELECT * FROM votes 
WHERE postID = :postid