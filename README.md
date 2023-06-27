# Airline-Management-System

This is a Django based website that targets to control an airline's operations. This website allows an airline company to manage data like checking and editing flight and passenger status. The project fetches the backend data from MySQL.✨

## Setting up this project
- Make sure Python and pip are installed. Install pip yourself to ensure you have the latest version:
  <br>```py -m pip install --upgrade pip```
  <br>```py -m pip --version```
- Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. Install virtualenv using pip:
  <br>```py -m pip install --user virtualenv```
- Create a virtual environment:
  <br>```py -m venv env```
- Activate this project's environment:
  <br>```.\env\Scripts\activate```
- If you want to deactivate the virtual environment, use:
  <br>```deactivate```
- Run ```pip install django``` to install Django
- Make a MySQL database using the code given in *database.txt*
- Check the settings.py file in the project folder and locate this code:<br>
  DATABASES = {<br>
    'default': {<br>
        'ENGINE': 'django.db.backends.mysql',<br>
        'NAME': 'flights',<br>
        'USER': 'root',<br>
        'HOST': 'localhost',<br>
        'PORT': '3306',<br>
        'PASSWORD': '1203',<br>
    }<br>
}<br>
Here use your own username, password of MySQL.
- Run `python manage.py makemigrations` to identify the changes you have made to the database model.
- Run `python manage.py migrate` to apply migrations.
- To connect database to MySQL Client run command `pip install mysqlclient`
- Start the development server using `python manage.py runserver`.

## Contributors

ISHIKA BANERJEE [@ishika-tia](https://github.com/ishika-tia) </br>
SUDHANSHU RANJAN [@sudhanshuranjan2002](https://github.com/sudhanshuranjan2002) 
