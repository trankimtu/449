-- :name list_sorted_by_score :many
select * FROM votes
where postID IN :postID
order by (upVoted - downVoted) desc