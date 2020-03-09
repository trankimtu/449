-- $ sqlite3 votes.db < votes.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS votes;
CREATE TABLE votes (
    id INTEGER primary key,
	postID INTEGER,
	upVoted INTEGER,
	downVoted INTEGER,
	communityID VARCHAR
);
INSERT INTO votes(id, postID, upVoted, downVoted, communityID) VALUES(1,10,0,0,'funny');
INSERT INTO votes(id, postID, upVoted, downVoted, communityID) VALUES(2,11,0,0,'python');
INSERT INTO votes(id, postID, upVoted, downVoted, communityID) VALUES(3,12,0,0,'homework');
INSERT INTO votes(id, postID, upVoted, downVoted, communityID) VALUES(4,13,0,0,'project');
INSERT INTO votes(id, postID, upVoted, downVoted, communityID) VALUES(5,14,0,0,'professor');
COMMIT;