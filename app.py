import os

from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = os.environ.get('MONGO_DB_URL', '')
client = MongoClient(mongo_uri)

db = client['my-db']
collection = db['my-collection']


@app.route('/', methods=['GET'])
def get_root():
    return "test"


@app.route('/data', methods=['GET'])
def get_data():
    documents = collection.find()
    data = []
    for document in documents:
        data.append({
            'id': str(document['_id']),
            'data': document.get('data')
        })
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
