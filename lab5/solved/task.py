import json

class Task:
    def __init__(self, id, name, description, priority) -> None:
        self.id = id
        self.name = name
        self.descriptiom = description
        self.priority = priority
        self.status = "not done"

    def __init__(self, json) -> None:
        self = self(**json)

    def toJson(self):
        return json.dumps(self.__dict__)
