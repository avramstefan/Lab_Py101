import requests
from task import Task

url = "http://127.0.0.1:5000/"

while True:
    command = input()
    if command == "Sanity check":
        x = requests.get(f"{url}sanity")
        print(x.status_code)
    elif command == "Add":
        task = Task(input('id='), input('name='), input('description='), "not done")
        print(task.toJson())
        requests.post(f"{url}add", json=task.toJson())
    elif command == "Print":
        task = requests.get(f"{url}print")
        print(task.text)
    elif command == "Print Employee Tasks":
        name = input("name=")
        task = requests.get(f"{url}print/" + name)
        print(task.text)
    elif command == "Print Pending Tasks":
        task = requests.get(f"{url}print/pending")
        print(task.text)
    elif command == "Print Completed Tasks":
        task = requests.get(f"{url}print/completed")
        print(task.text)
    elif command == "Delete":
        id = input('id=')
        requests.delete(f"{url}delete/" + id)
    elif command == "Delete All":
        requests.delete(f"{url}delete/all")
    elif command == "Complete Task":
        id = input("id=")
        requests.post(f"{url}update/" + id)
    elif command == "Change Task Assignee":
        id = input("id=")
        name = input("name=")
        requests.post(f"{url}update/" + id + "/" + name)
    elif command == "Save":
        requests.post(f"{url}save")
    elif command == "Load":
        requests.post(f"{url}load")
    elif command == "Exit":
        break
