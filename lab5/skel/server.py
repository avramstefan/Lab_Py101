from flask import Flask
from flask import jsonify, request
import json

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
    # Read the json from the request
    j =  json.loads(request.get_json())
    # TO DO add task to database
    
    
    # Send response
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#3
@app.route('/print', methods=['GET'])
def showTasks():
    # TO DO return database in json format
    pass


#3.1
@app.route('/print/<name>', methods=['GET'])
def showEmployeeTasks(name):
    # TO DO search for tasks that have the employyes name
    # return them in json format
    pass

#3.2
@app.route('/print/pending', methods=['GET'])
def showPendingTasks():
    # TO DO search for tasks that have status not done
    # return them in json format
    pass

#3.3
@app.route('/print/completed', methods=['GET'])
def showCompletedTasks():
    # TO DO search for tasks that have status completed
    # return them in json format
    pass

#4
@app.route('/delete/<id>', methods=['DELETE'])
def deleteTask(id):
    # TO DO delete the task that has the id id from the database
    pass

#4.1
@app.route('/delete/all', methods=['DELETE'])
def deleteAllTasks():
    # TO DO clear database
    pass

#5
@app.route('/update/<id>', methods=['POST'])
def updateTaskStatus(id):
    # TO DO change task status to completed
    pass

#5.1
@app.route('/update/<id>/<name>', methods=['POST'])
def updateTaskAssignee(id, name):
    # TO DO change task asignee
    pass

#6
@app.route('/save', methods=['POST'])
def saveTasks():
    # TO DO store database to a json file
    pass

#7
@app.route('/load', methods=['POST'])
def loadTasks():
    # TO DO load database from json file
    pass

