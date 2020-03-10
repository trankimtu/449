import flask_api
from flask import request
from flask_api import status, exceptions
import pugsql


app = flask_api.FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')

queries = pugsql.module('queries/')
queries.connect(app.config['DATABASE_URL'])


@app.cli.command('init')
def init_db():
    with app.app_context():
        db = queries._engine.raw_connection()
        with app.open_resource('posts.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        with app.open_resource('votes.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Post Get Delete ... home page</h1>'''
    

@app.route('/posts/all', methods=['GET'])
def all_posts():
    all_posts = queries.all_posts()
    return list(all_posts)

@app.route('/posts/<int:PostID>', methods=['GET'])
def post_ID(PostID):
    post = queries.post_by_id(PostID=PostID)
    if post:
        return post
    else:
        raise exceptions.NotFound()
@app.route('/posts', methods=['GET', 'POST'])
def n_recent_posts():
    if request.method == 'GET':
        n = request.args.get('n', 5)
        post = queries.n_post_by_time(n=n)
        if post:
            return list(post)
        else:
            raise exceptions.NotFound()

        # return filter_posts(request.args)
    elif request.method == 'POST':
        return create_post(request.data)


def create_post(post):
    required_fields = ['Username', 'PostTitle', 'Content', 'Community', 'URLResource']

    if not all([field in post for field in required_fields]):
        raise exceptions.ParseError()
    try:
        post['PostID'] = queries.create_post(**post)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT

    return post, status.HTTP_201_CREATED, {
        'Location': f'/posts/{post["PostID"]}'
    }

def filter_posts(query_parameters):
    PostID      = query_parameters.get('PostID')
    Username    = query_parameters.get('Username')
    PostTitle   = query_parameters.get('PostTitle')
    PostDate    = query_parameters.get('PostDate')
    Content     = query_parameters.get('Content')
    Community   = query_parameters.get('Community')
    URLResource = query_parameters.get('URLResource')


    query = "SELECT * FROM posts WHERE"
    to_filter = []

    if PostID:
        query += ' PostID=? AND'
        to_filter.append(PostID)
    if Username:
        query += ' Username=? AND'
        to_filter.append(Username)
    if PostTitle:
        query += ' PostTitle=? AND'
        to_filter.append(PostTitle)
    if PostDate:
        query += ' PostDate=? AND'
        to_filter.append(PostDate)
    if Content:
        query += ' Content=? AND'
        to_filter.append(Content)
    if Community:
        query += ' Community=? AND'
        to_filter.append(Community)
    if URLResource:
        query += ' URLResource=? AND'
        to_filter.append(URLResource)
    if not (PostID or Username or PostTitle or PostDate or Content or Community or URLResource):
        raise exceptions.NotFound()

    query = query[:-4] + ';'

    results = queries._engine.execute(query, to_filter).fetchall()

    return list(map(dict, results))

    


@app.route('/posts/delete/<int:PostID>', methods=['GET', 'DELETE'])
def delete(PostID):
    if request.method == 'DELETE':
        delquery = queries.delete_by_id(PostID=PostID)

        #delquery return number rows of delete
        # check if it's 0 or not


        if delquery == 0:
            raise exceptions.NotFound()
        else:
            return '', status.HTTP_204_NO_CONTENT
    else:
        return {'status': 'OK'}









# List the n most recent posts to a particular community

@app.route('/posts/<string:Community>', methods=['GET'])
def post_by_community(Community):
    n = request.args.get('n',3)
    post = queries.post_by_community(Community=Community,n=n)
    if post:
        return list(post)
    else:
        raise exceptions.NotFound()






# http://localhost:5000/posts?n=10
# http://localhost:5000/posts/Community_3?n=3
