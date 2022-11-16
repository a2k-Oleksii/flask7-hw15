Python classes practice
Homework
Create models, views and forms for Plants
Create simple templates (for example you have auth logic)
Local setup
Create python environment

$ python3 -m venv .venv
Activate python environment

$ source .venv/bin/activate
Install dependencies

$ pip install -r requirements.txt
Run database container

Rename file .env.sample in .env

$ docker-compose up -d db
Add migrations to database

$ flask db migrate
Run application

$ flask run
Setup with docker
$ docker-compose up -d --build

1. Create app.models.plant.py, views.plant.py, app.forms.plant.py
2. Create templates plants.html, plant.register.html, plant.profile.html

App has menu 'Plants'. This menu has two button 'Add plant' and 'Information about plants'.
If you choise 'Add plant' it starts registration form
If oyu choise "Information about plants" is input information about all plants.