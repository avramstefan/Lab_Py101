import requests
from task import Task

while True:
    command = input()
    if command == "Sanity check":
        x = requests.get("http://127.0.0.1:5000/sanity")
        print(x.status_code)
    elif command == "Add":
        task = Task(input('id='), input('name='), input('description='), input('priority='), "not done")
        print(task.toJson())
        requests.post("http://127.0.0.1:5000/add", json=task.toJson())
    elif command == "Print":
        task = requests.get("http://127.0.0.1:5000/print")
        print(task.text)
    elif command == "Print Employee Tasks":
        name = input("name=")
        task = requests.get("http://127.0.0.1:5000/print/" + name)
        print(task.text)
    elif command == "Print Pending Tasks":
        task = requests.get("http://127.0.0.1:5000/print/pending")
        print(task.text)
    elif command == "Print Completed Tasks":
        task = requests.get("http://127.0.0.1:5000/print/completed")
        print(task.text)
    elif command == "Delete":
        id = input('id=')
        requests.delete("http://127.0.0.1:5000/delete/" + id)
    elif command == "Delete All":
        requests.delete("http://127.0.0.1:5000/delete/all")
    elif command == "Complete Task":
        id = input("id=")
        requests.post("http://127.0.0.1:5000/update/" + id)
    elif command == "Change Task Assignee":
        id = input("id=")
        name = input("name=")
        requests.post("http://127.0.0.1:5000/update/" + id + "/" + name)
    elif command == "Save":
        requests.post("http://127.0.0.1:5000/save")
    elif command == "Load":
        requests.post("http://127.0.0.1:5000/load")
    elif command == "Exit":
        break
