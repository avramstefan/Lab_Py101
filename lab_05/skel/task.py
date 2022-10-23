import json

class Task:
    """
    Attributes:
        id: identificator unic, folosit drept cheie in database.
        type: int
        name: numele persoanei careia i-a fost asignat task-ul.
        type: string
        description: scurta descriere a task-ului.
        type: string
        status: are valoarea not done sau completed
        type: string
    """
    def __init__(self, id, name, description, priority, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def toJson(self):
        return json.dumps(self.__dict__)
