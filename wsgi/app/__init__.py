from flask import Flask,jsonify
app = Flask('testing application') 

mytasks = [
{
'id': 1,
'task': u'Finish Hello World',
'session': u'Week 7','done': True
}
,
{'id': 2,'task': u'Finish first API',
'session': u'Week 7','done': False}]
@app.route('/api', methods=['GET'])

def api():
	return jsonify({'tasks': mytasks})
#from app import views
