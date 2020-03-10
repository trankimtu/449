-- :name create_post :insert
INSERT INTO posts(Username, PostTitle, Content, Community, URLResource)
VALUES(:Username, :PostTitle, :Content, :Community, :URLResource);


