# EHPADdjango

## Requirements

### Create the project
#### Select the folder
cd EHPADdjango  
#### Create Live Environment
python3 -m venv LiveEnv 

### Install and activate the project 
#### Activate environment
source LiveEnv/bin/activate  

#### install django
pip install django     
pip install --upgrade pip  

#### install mysql connector
pip install mysql-connector-python

#### create live app
python manage.py startapp LiveApp 

#### run server
python3 manage.py runserver

#### Database settings and credentials

Please create a .env file at the root of the project with the following information : 

`
DATABASE_NAME = 'ehpaddjango'
DATABASE_USER = 'name_of_your_user'
DATABASE_PASS = 'password_of_your_user'
DATABASE_PORT = 'your_database_port'
DATABASE_HOST = 'your_database_host'
`

#### Make the migrations 
python3 manage.py makemigrations
python3 manage.py migrate
