import requests

url = "http://127.0.0.1:5000/"

while True:
    command = input()
    if command == "Sanity check":
        x = requests.get(f"{url}sanity")
        print(x.status_code)
    elif command == "Add":
        pass
    elif command == "Print":
        pass
    elif command == "Print Employee Tasks":
        pass
    elif command == "Print Pending Tasks":
        pass
    elif command == "Print Completed Tasks":
        pass
    elif command == "Delete":
        pass
    elif command == "Delete All":
        pass
    elif command == "Complete Task":
        pass
    elif command == "Change Task Assignee":
        pass
    elif command == "Save":
        pass
    elif command == "Load":
        pass
    elif command == "Exit":
        break
