import json

class Task:
    def __init__(self, id, name, description, priority, status) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status

    def toJson(self):
        return json.dumps(self.__dict__)
