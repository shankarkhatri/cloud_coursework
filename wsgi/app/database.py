from app import app
from flask_pymongo import PyMongo
from flask import jsonify
import os

app.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL'] + os.environ['OPENSHIFT_APP_NAME']

mongo = PyMongo(app)

@app.route('/database/collections', methods=['GET'])
def get_all_databases():
	return jsonify({'result' : mongo.db.collection_names()})


@app.route('/database/personnel', methods=['GET'])
def getallpersonnel():
	collection = mongo.db.test
	output = []
	for doc in collection.find():
		output.append({'Who' : doc['Name'], 'Job Role' : doc['Profession']})

	return jsonify({'result' : output})


@app.route('/database/users', methods=['GET'])
def getallusers():
	collection = mongo.db.users
	output = []
	for doc in collection.find():
		output.append({'Username' : doc['username'], 'Account Type' : doc['type']})

	return jsonify({'result' : output})


@app.route('/database/add', methods=['GET'])
def insert_into_db():
        collection = mongo.db.test
	collection.insert_one({'Name': 'TestingName', 'Profession': 'student'})
	return jsonify({'result' : 'successfull'})


@app.route('/database/addusers', methods=['GET'])
def insert_into_db_users():
        collection = mongo.db.users
	collection.drop()
	collection.insert_one({'username': 'admin', 'password': 'admin123','type':'admin'})
	collection.insert_one({'username': 'user', 'password': 'user123','type':'user'})
	return jsonify({'result' : 'successfull'})

#OPENSHIFT_APP_NAME=sk323apitest1
#mongodb://admin:7jyadjEqTRHl@127.2.167.2:27017/
