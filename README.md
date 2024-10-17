<h1>Django RestFramwork Blog App</h1>
<h3">A Blog app project, based on Django and Django Rest Framework using classed base view (modelviewset) and jwt authentication for user accounts</h3>

### Overview
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Getting ready](#getting-ready)
- [options](#options)
- [Api and Documents](#api-and-documents)
- [Reformat and check](#reformat-and-check)
- [Bugs or Opinion](#bugs-or-opinion)

### Features
- Django LTS
- Class Based View
- Django RestFramework
- ModelViewSet
- JWT Authentication
- SimpleJWT
- Custom User Model
- Black
- Flake8


### Setup
Clone the repo
```bash
git clone https://github.com/prz95/Django-DRF-ToDoApp.git
```

### Getting ready
Create an enviroment
```bash
python -m venv venv
```

Run the following command to install all dependencies of the project
```bash
pip install -r requirements.txt
```

go to the repo directory and run the following command

```bash
python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python manage.py migrate
```

### options
In order to use the admin panel you need to create a super user.you can use the createsuperuser option to make a super user.
```bash
python manage.py createsuperuser
```

Start the server by following command

```bash
python manage.py runserver
```

Once the server is up and running, head over to http://127.0.0.1:8000/admin for the Admin Panel. 

### Api and Documents
in order to use the api in document format you can simply head to this url

http://127.0.0.1:8000/swagger/

<p align="center">
<img src="" alt="swagger document" width="720"/>
</p>


### Reformat and check
If you want your code to be check by pep8 and all the guide lines, there are two packages added to requirements in order to check and reformat code.
you can use it by this command:
```bash
black -l 79 . && flake8
```

### Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.