# Science Fiction Novel API from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#
# What's new:
#
#  * Switched from Flask to Flask API
#    <https://www.flaskapi.org>
#
#  * Switched to PugSQL for database access
#    <https://pugsql.org>
#
#  * SQLAlchemy Database URL specified in app config file
#
#  * Adds CLI command to create initial schema from "Using SQLite 3 with Flask"
#    <https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/>
#
#  * New API calls:
#    - GET /api/v1/resources/votes/{id} to retrieve a specific vote
#    - POST /api/v1/resources/votes to create a new vote
#

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
        with app.open_resource('votes.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

# view all votes http://127.0.0.1:5000/api/v1/resources/votes/all
@app.route('/api/v1/resources/votes/all', methods=['GET'])
def all_votes():
    all_votes = queries.all_votes()

    return list(all_votes), status.HTTP_200_OK

# view vote by id http://127.0.0.1:5000/api/v1/resources/votebyid/1
@app.route('/api/v1/resources/votebyid/<int:id>', methods=['GET'])
def vote_by_id(id):
    vote = queries.vote_by_id(id=id)
    if vote:
        return vote, status.HTTP_200_OK
    else:
        raise exceptions.NotFound()

# view vote by postid http://127.0.0.1:5000/api/v1/resources/votesbypostid/10
@app.route('/api/v1/resources/votesbypostid/<int:postid>', methods=['GET'])
def vote_by_postid(postid):
    vote = queries.vote_by_postid(postid=postid)
    if vote:
        return vote, status.HTTP_200_OK
    else:
        raise exceptions.NotFound()

# top n post score http://127.0.0.1:5000/api/v1/resources/toppostscore/3
@app.route('/api/v1/resources/toppostscore/<int:topscore>', methods=['GET'])
def top_post_score(topscore):
    top = queries.top_post_score(topscore=topscore)
    if top:
        return list(top), status.HTTP_200_OK
    else:
        raise exceptions.NotFound()

# up_vote a post by postID http://127.0.0.1:5000/api/v1/resources/upvote
# input ex {"postID": 10}
@app.route('/api/v1/resources/upvote', methods=['GET', 'POST'])
def up_votes():
    if request.method == 'GET':
        return filter_votes(request.args)
        # return up_vote(request.data)
    elif request.method == 'POST':
        return up_vote(request.data)

def up_vote(vote):
    required_fields = ['postID']
    if not all([field in vote for field in required_fields]):
        raise exceptions.ParseError()
    vote_update = queries.up_vote(**vote)
    # return {'updated': vote_update}, status.HTTP_200_OK
    return filter_votes(vote), status.HTTP_200_OK

def filter_votes(query_parameters):
    postID = query_parameters.get('postID')
    query = "SELECT * FROM votes WHERE"
    to_filter = []

    if postID:
        query += ' postID=? AND'
        to_filter.append(postID)
    if not (postID):
        raise exceptions.NotFound()

    query = query[:-4] + ';'
    results = queries._engine.execute(query, to_filter).fetchall()
    return list(map(dict, results))

# down_vote a post by postID http://127.0.0.1:5000/api/v1/resources/downvote
# input ex {"postID": 11}
@app.route('/api/v1/resources/downvote', methods=['GET', 'POST'])
def down_votes():
    if request.method == 'GET':
        return filter_votes(request.args)
        # return down_vote(request.data)
    elif request.method == 'POST':
        return down_vote(request.data)

def down_vote(vote):
    required_fields = ['postID']
    if not all([field in vote for field in required_fields]):
        raise exceptions.ParseError()
    down_vote_update = queries.down_vote(**vote)
    return filter_votes(vote), status.HTTP_200_OK

# list sorted by score http://127.0.0.1:5000/api/v1/resources/listsortedbyscore
#input example: {"list": [10, 13, 15]}
@app.route('/api/v1/resources/listsortedbyscore', methods=['GET', 'POST'])
def list_sorted():
    if request.method == 'GET':
        return filter_votes(request.args)
    elif request.method == 'POST':
        return list_sorted_by_score(request.data)

def list_sorted_by_score(listPostID):
    print(listPostID)
    list_sorted = queries.list_sorted_by_score(postID=listPostID['listID'])
    return list(list_sorted), status.HTTP_200_OK

