-- :name create_vote :insert
INSERT INTO vote(postID, upVoted, downVoted)
VALUES(:postID, :upVoted, :downVoted)
