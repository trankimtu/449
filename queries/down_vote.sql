-- :name down_vote :affected
UPDATE votes SET downVoted = (downVoted + 1) 
WHERE postID = :postID