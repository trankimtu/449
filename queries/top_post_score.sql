-- :name top_post_score :many
SELECT * FROM votes 
ORDER BY (upVoted - downVoted) desc
LIMIT :topscore