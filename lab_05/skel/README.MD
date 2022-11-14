# SetUp

Vom folosi un virtual environment pentru acest laborator.

Ce este un virtual environment?

Este o unealta care ne ajuta sa separam dependentele mai multor proiecte, creand medii virtuale pentru ele. 

Pe scurt, un virtual environment ne permite sa instalam dependinte numai pentru proiectul la care lucram.
Dependintele globale nu sunt vizibile in proiectul curent si dependintele proiectului curent nu sunt vizibile pentru alte proiecte.

Mai multe informatii gasesti aici: https://www.geeksforgeeks.org/python-virtual-environment/

Pentru acest proiect avem nevoie sa instalam flask.

## Windows
Deschide un terminal si urmeaza pasii:

### Creaza un virtual environment

```
> py -3 -m venv skel
```

### Activeaza mediul virtual

```
> skel\Scripts\activate
```

Configuratia de windows standard are scripturile blocate. Daca comanda asta nu merge inseamna ca trebuie sa-ti activezi
executarea scripturilor. 

https://superuser.com/questions/106360/how-to-enable-execution-of-powershell-scripts 

### Install Flask

```
> pip install Flask 
```
S-ar putea sa ai nevoie si de request.
In alt terminal ruleaza:

```
> pip install request
```
## Linux/Mac OS
Deschide un terminal in lab_05 si urmeaza pasii:

### Creaza un virtual environment

```
$ python3 -m venv skel
```

### Activeaza mediul virtual

```
$ ./skel/bin/activate
```

### Install Flask

```
$ pip install Flask
```
S-ar putea sa ai nevoie si de request.
In alt terminal ruleaza:

```
$ pip install request
```
# Task

Foloseste comanda flask --app server run pentru a pornii server-ul.
Foloseste python3 client.py pentru client.

Vom crea o aplicatie de tipul task manager, pentru o companie care are nevoie sa-si organizeze angajatii.

Aplicatia va avea:

Un server care stocheaza informatii despre task-uri.

Un client care va face cereri catre server pentru a interoga/modifica baza de date.

Va punem la dispozitie clasa Task de care ne vom folosi in cadrul acestui laborator pentru
a reprezenta informatiile ce trebuie stocate in baza de date.
Baza de date va fi un dictionar in care cheia va fi id-ul task-ului iar valoarea va fi un
alt dictionar construit pe baza clasei Task.
Mai multe informatii gasiti in fisierul task.py.

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

Scopul acestei cereri este de a verifica ca serverul functioneaza, si este deja
implementata de noi.

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

Clientul trimite un json cu date despre un task.
Serverul primeste cererea, tranforma datele din body intr-o instanta a clasei
task.
Si acest exercitiu este deja implementat.

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

Clientul va afisa in terminal raspunsul de la server.

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

Clientul va afisa in terminal raspunsul de la server.

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

Clientul va afisa in terminal raspunsul de la server.

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

Clientul va afisa in terminal raspunsul de la server.

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

Serverul va salva baza de date intr-un fisier de tip json.

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
