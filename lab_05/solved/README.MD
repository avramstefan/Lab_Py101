# Set Up

Vom folosi un virtual environment pentru acest laborator.

Ce este un virtual environment?

Este o unealta care ne ajuta sa separam dependintele mai multor proiecte, creand medii virtuale pentru ele. 

Pe scurt, un virtual environment ne permite sa instalam dependinte numai pentru proiectul la care lucram.
Dependintele globale nu sunt vizibile in proiectul curent si dependintele proiectului curent nu sunt vizibile pentru alte proiecte.

Mai multe informatii gasesti aici: https://www.geeksforgeeks.org/python-virtual-environment/

Pentru acest proiect avem nevoie sa instalam flask.

## Windows
Deschide o linie de comanda si urmeaza pasii:

### Creaza un virtual environment

```
> mkdir myproject
> cd myproject
> py -3 -m venv solved
```

### Activeaza mediul virtual

```
> venv\Scripts\activate
```

Configuratia de windows standard are scripturile blocate. Daca comanda asta nu merge inseamna ca trebuie sa-ti activezi
executarea scripturilor. 

https://superuser.com/questions/106360/how-to-enable-execution-of-powershell-scripts 

### Install Flask

```
> pip install Flask
```

## Linux/Mac OS
Deschide o linie de comanda si urmeaza pasii:

### Creaza un virtual environment

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activeaza mediul virtual

```
$ . venv/bin/activate
```

### Install Flask

```
$ pip install Flask
```
S-ar putea sa ai nevoie si de request:

```
pip install request
```
# Task

Foloseste comanda flask --app server run pentru a pornii server-ul.
Foloseste python3 client.py pentru client.

Vom crea o aplicatie de tipul task manager, pentru o companie care are nevoie sa-si organizeze angajatii.

Aplicatia va avea:

Un server care stocheaza informatii despre task-uri.

Un client care va face cereri catre server pentru a interoga/modifica baza de date.

In cadrul acestui laborator baza de date este reprezentata de un dictionar.

Va trebui sa implementati urmatoarele cereri:

## 1. Sanity
Url: http://127.0.0.1:5000/sanity

Type: Get
```
Body:
{

}
```
```
Response:
{
    "Status": "Up"
}
```

## 2. Add Task
Url: http://127.0.0.1:5000/add

Type: Post

```
Body:
{
    "id": "id"
    "name": "name of employe"
    "description": "description"
    "priority": "priority"
    "status": "not done"
}
```

```
Response:
{
    "status_code": "200"
}
```

## 3. Print Tasks

Url: http://127.0.0.1:5000/print

Type: Get

```
Body:
{

}
```
```
Response: Json containing all tasks stored in the database
```

## 3.1. Print Employee Tasks

Url: http://127.0.0.1:5000/print/name

Type: Get

```
Body:
{

}
```
```
Response: Json containing all tasks of the employee with the name: "name" stored in the database
```

## 3.2. Print Pending Tasks

Url: http://127.0.0.1:5000/print/pending

Type: Get

```
Body:
{

}
```
```
Response: Json containing all tasks with status not done.
```

## 3.3. Print Completed Tasks

Url: http://127.0.0.1:5000/print/completed

Type: Get

```
Body:
{

}
```
```
Response: Json containing all tasks with status completed.
```

## 4. Delete Task

Url: http://127.0.0.1:5000/delete/id

Type: Delete

```
Body:
{

}
```
```
Response:
{
    "status_code": "200"
}
```

Sterge task-ul cu id-ul dat.

## 4.1. Delete All Tasks

Url: http://127.0.0.1:5000/delete/all

Type: Delete

```
Body:
{

}
```
```
Response:
{
    "status_code": "200"
}
```

Sterge toate task-urile din baza de date.

## 5. Update Task

Url: http://127.0.0.1:5000/update/id

Type: Post

```
Body:
{

}
```
```
Response:
{
    "status_code": "200"
}
```

Updateaza statusul task-ul cu id-ul dat.

## 5.1 Update Task Assignee

Url: http://127.0.0.1:5000/update/id/name

Type: Post

```
Body:
{

}
```
```
Response:
{
    "status_code": "200"
}
```

Updateaza numele persoanei din task-ul cu id-ul dat.

## 6. Save

Url: http://127.0.0.1:5000/save

Type: Post

```
Body:
{

}
```
```
Response:
{
    "status_code": "200"
}
```

Serverul va salva.

## 7. Load

Url: http://127.0.0.1:5000/load

Type: Post

```
Body:
{

}
```
```
Response:
{
    "status_code": "200"
}
```

Serverul va incarca baza de date dintr-un fisier json.

## 8. Bonus

Testeaza serverul folosind Postman
