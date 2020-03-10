-- :name up_vote :affected
UPDATE votes SET upVoted = (upVoted + 1) 
WHERE postID = :postID