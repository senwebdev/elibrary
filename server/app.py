from flask import Flask, jsonify, request, json
from flask_cors import CORS
import uuid
from pymongo import MongoClient
from flask_pymongo  import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

DEBUT=True

app=Flask(__name__)
app.config.from_object(__name__)
app.config['MONGO_DBNAME'] = 'blog'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/blog'
app.config['JWT_SECRET_KEY'] = 'secret'

CORS(app)

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
client = MongoClient('localhost:27017')
db = client.blog

@app.route('/users/register', methods=['POST'])
def register():
    users = mongo.db.users
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()

    user_id = users.insert({
	'first_name' : first_name, 
	'last_name' : last_name, 
	'email' : email, 
	'password' : password, 
	'created' : created, 
	})
    new_user = users.find_one({'_id' : user_id})

    result = {'email' : new_user['email'] + ' registered'}
    return jsonify({'result' : result})
	

@app.route('/users/login', methods=['POST'])
def login():

    users = mongo.db.users
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""
	
    response = users.find_one({'email' : email})

    if response:	
        if bcrypt.check_password_hash(response['password'], password):
            access_token = create_access_token(identity = {
			    'first_name': response['first_name'],
				'last_name': response['last_name'],
				'email': response['email']}
				)
            result = access_token
        else:
            result = jsonify({"error":"Invalid username and password"})
    else:
        result = jsonify({"result":"No results found"})
    
    return result
	
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        insert_book(post_data)
        response_object['message'] = 'Book added!'
    else:
        # convert to dict 
        response_object['books'] = json.loads(read_book(''))
        # convert to string
        response_object = json.dumps(response_object)
    return response_object

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        insert_book(post_data)
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return json.dumps(response_object, default=lambda o: o.__dict__)

@app.route('/search', methods=['GET'])
def search_book():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        search_key = request.args.get('search_key')
        response_object = json.loads(read_book(search_key))
    return json.dumps(response_object)

@app.route('/latest_books', methods=['GET'])
def latest_books():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        response_object = json.loads(get_latest_books())
    return json.dumps(response_object)

@app.route('/popular_books', methods=['GET'])
def popular_books():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        response_object = json.loads(get_popular_books())
    return json.dumps(response_object)

def read_book(search_key):
    if search_key == "":
        cursor = db.bookdata1.find()
    else:
        cursor = db.bookdata1.find({"$or" : [
            {"_id" : {"$regex": search_key, '$options': 'i'}},
            {"title" : {"$regex": search_key, '$options': 'i'}},
            {"author" : {"$regex": search_key, '$options': 'i'}}
        ] })
    # transform pymongo cursor to string
    return dumps(cursor)

def insert_book(newBook): 
    col = db.bookdata1
    col.insert_one(
        {
            "_id": uuid.uuid4().hex,
            "title": newBook.get('title'),
            "author": newBook.get('author'),
            "available": newBook.get('available')
        }
    )

def remove_book(book_id):
    col = db.bookdata1
    col.delete_one({"_id": book_id})

def get_latest_books(): 
    cursor = mongo.db.bookdata1.find().sort([('$natural', -1)]).limit(8)
    return dumps(cursor)

def get_popular_books(): 
    cursor = mongo.db.bookdata1.find().sort("likes", -1).limit(8)
    return dumps(cursor)

if __name__ == '__main__':
	app.run()
 