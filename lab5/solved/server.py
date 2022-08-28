from flask import Flask
from flask import jsonify, request
import json
from task import Task

app = Flask(__name__)
database = {}

#1
@app.route('/sanity', methods=['GET'])
def hello_world():
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#2
@app.route('/add', methods=['POST'])
def addTask():
    j =  json.loads(request.get_json())
    task = Task(j)
    database[task.id] = task.__dict__
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#3
@app.route('/print', methods=['GET'])
def showTasks():
    return json.dumps(database)

@app.route('/<id>', methods=['DELETE'])
def deleteTask(id):
    print(id)
    if id in database:
        database.pop(id)
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response
