import requests
from task import Task

while True:
    command = input()
    if command == "Sanity check":
        x = requests.get("http://127.0.0.1:5000/sanity")
        print(x.text)
    elif command == "Add":
        task = Task(input('id='), input('name='), input('deadline='), input('priority='))
        print(task.toJson())
        requests.post("http://127.0.0.1:5000/add", json=task.toJson())
    elif command == "Print":
        task = requests.get("http://127.0.0.1:5000/print")
        print(task.text)
    elif command == "Delete":
        id = input('name=')
        requests.delete("http://127.0.0.1:5000/" + id)
    elif command == "Exit":
        break
