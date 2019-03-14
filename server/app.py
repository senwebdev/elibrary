from flask import Flask, jsonify, request, json
from flask_cors import CORS
import uuid
from pymongo import MongoClient
from bson.json_util import dumps

DEBUT=True

app=Flask(__name__)
app.config.from_object(__name__)
app.config.update(
)

CORS(app)

client = MongoClient('localhost:27017')
db = client.blog

def read_book(search_key):
    if search_key == "":
        cursor = db.bookdata.find()
    else:
        cursor = db.bookdata.find({"$or" : [
            {"title" : {"$regex": search_key, '$options': 'i'}},
            {"author" : {"$regex": search_key, '$options': 'i'}}
        ] })
    # transform pymongo cursor to string
    return dumps(cursor)

def insert_book(newBook):
    col = db.bookdata
    col.insert_one(
        {
            "_id": uuid.uuid4().hex,
            "title": newBook.get('title'),
            "author": newBook.get('author'),
            "read": newBook.get('read')
        }
    )

def remove_book(book_id):
    col = db.bookdata
    col.delete_one({"_id": book_id})
	
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

if __name__ == '__main__':
	app.run()
