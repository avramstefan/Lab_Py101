# Set Up

We will use a virtual enviroment for this lab.

What is a virtual enviorement?

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

TLDR: with a virtual envioremet we download dependencies only for the project we are currently working with. We don't use the globally installed dependencies, and the dependencies that we install are not visible in other projects.

Read more about virtual enviorements here: https://www.geeksforgeeks.org/python-virtual-environment/

For this project we need to have flask and it's dependencies installed.

## Windows
Oppen a comand line, and follow this steps:

### Create an environment

```
> mkdir myproject
> cd myproject
> py -3 -m venv venv
```

### Activate the environment

```
> venv\Scripts\activate
```

On windows scripts are disabled by default. If this command does not work enable scripts. 

https://superuser.com/questions/106360/how-to-enable-execution-of-powershell-scripts 

### Install Flask

```
> pip install Flask
```

## Linux/Mac OS
Oppen a comand line, and follow this steps:

### Create an environment

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activate the environment

```
$ . venv/bin/activate
```

### Install Flask

```
$ pip install Flask
```
You may also need to install request:

```
pip install request
```
# Task

We are going to create a task management web application for a company that needs to organize its emploies.

The manager of the project wants to have the following features.

A server that stores information about the tasks.

A client witch will send request to the server to interogate and modify the database.

You will have to implement the following request

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

Url: http://127.0.0.1:5000/print/name

Type: Get

```
Body:
{

}
```
```
Response: Json containing all tasks with status not done.
```

## 3.2. Print Completed Tasks

Url: http://127.0.0.1:5000/print/name

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

Delete the task with the id: id from the databese.

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

Delete all tasks from the databese.

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

Update the task status with the id: id to completed from not done.

## 5.1 Update Task Assignee

Url: http://127.0.0.1:5000/update/id

Type: Post

```
Body:
{
    "name": "name"
}
```
```
Response:
{
    "status_code": "200"
}
```

Update the task name with the id: id.

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

The server will save the database in a file.

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

The server will load the database from a file.

## 8. Bonus

Use Postman to test the server.
