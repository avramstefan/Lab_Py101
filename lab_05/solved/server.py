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
    task = Task(**j)
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

#3.1
@app.route('/print/<name>', methods=['GET'])
def showEmployeeTasks(name):
    answer = {}
    for task in database.values():
        if name == task['name']:
            answer[task['id']] = task
    return json.dumps(answer)

#3.2
@app.route('/print/pending', methods=['GET'])
def showPendingTasks():
    answer = {}
    for task in database.values():
        if task['status'] == "not done":
            answer[task['id']] = task
    return json.dumps(answer)

#3.3
@app.route('/print/completed', methods=['GET'])
def showCompletedTasks():
    answer = {}
    for task in database.values():
        if task['status'] == "completed":
            answer[task['id']] = task
    return json.dumps(answer)

#4
@app.route('/delete/<id>', methods=['DELETE'])
def deleteTask(id):
    if id in database:
        database.pop(id)
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#4.1
@app.route('/delete/all', methods=['DELETE'])
def deleteAllTasks():
    database.clear()
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#5
@app.route('/update/<id>', methods=['POST'])
def updateTaskStatus(id):
    if id in database:
        database[id]['status'] = "completed"
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#5.1
@app.route('/update/<id>/<name>', methods=['POST'])
def updateTaskAssignee(id, name):
    if id in database:
        database[id]['name'] = name
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#6
@app.route('/save', methods=['POST'])
def saveTasks():
    j = json.dumps(database)
    json_file = open("database.json","w")
    json_file.write(j)
    json_file.close
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#7
@app.route('/load', methods=['POST'])
def loadTasks():
    json_file = open("database.json","r")
    global database
    database = json.load(json_file)
    json_file.close
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

