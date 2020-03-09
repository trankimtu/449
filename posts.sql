-- $ sqlite3 posts.db < posts.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    PostID INTEGER primary key,
    Username VARCHAR,
    PostTitle VARCHAR,
    PostDate date DEFAULT CURRENT_TIMESTAMP,
    Content VARCHAR,
    Community VARCHAR,
    URLResource VARCHAR,
    UNIQUE(Username)
);
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 1','Post Title 1', 'Content 1', 'Community_1', 'www.URLResource1.com');
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 2','Post Title 2', 'Content 2', 'Community_2', 'www.URLResource2.com');
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 3','Post Title 3', 'Content 3', 'Community_3', 'www.URLResource3.com');
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 4','Post Title 4', 'Content 4', 'Community_1', 'www.URLResource4.com');
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 5','Post Title 5', 'Content 5', 'Community_2', 'www.URLResource5.com');
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 6','Post Title 6', 'Content 6', 'Community_2', 'www.URLResource6.com');
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 7','Post Title 7', 'Content 7', 'Community_1', 'www.URLResource7.com');
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 8','Post Title 8', 'Content 8', 'Community_2', 'www.URLResource8.com');
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource) VALUES('User 9','Post Title 9', 'Content 9', 'Community_3', 'www.URLResource9.com');
COMMIT;