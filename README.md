Movies REST API
-
Small REST API with CRUD actions for movies, actors and directors with rest.py script to be used to interact with API

by Łukasz Paciorek

-------------
Technologies used:
- 
- Python 3.8
- Django 4.0.2
- Django rest framework 3.13.1
- Requests 2.27.1
- Database on sqlite3

Configuration before first run:
- 
- configure virtual environment in Python:
    - virtualenv environment_name
    - install modules from requirements.txt (pip install -r requirements.txt)
- download master from repo
- django migrations(python3 manage.py makemigrations, python3 manage.py migrate)
- django create super user
- run django server(python3 manage.py runserver)

----------------
----------------
Main Features:  
-
- CRUD actions for models Movie, Actor, Director
- rest.py script for interaction with API (use --help argument for help)

----------------  
----------------
Modules
-

Api
-
- get all Movie, Actor Director data
- get specified Movie, Actor Director data
- create Movie, Actor Director
- modify Movie, Actor Director
- delete Movie, Actor Director


Form of project:
-
- full REST api endpoints (to interact with by rest.py script or to download with json and test with postman)