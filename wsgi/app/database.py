from app import app 
from flask_pymongo import PyMongo
from flask import jsonify
import os

#app.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
#app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL']

app.config['MONGO_DBNAME'] = "sk323apitest1"
app.config['MONGO_URI'] = "mongodb://admin:7jyadjEqTRHl@127.0.0.1:27017/sk323apitest1"
mongo = PyMongo(app)

@app.route('/database/collections', methods=['GET'])
def get_all_databases():
	return jsonify({'result' : mongo.db.collection_names()})
