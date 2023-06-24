# Airline-Management-System

This is a Django based website that targets to control an airline's operations. This website allows an airline company to manage data like checking and editing flight and passenger status.✨

## Setting up this project
- Make sure `python` and `pip` are installed. Install pip yourself to ensure you have the latest version:
  ```py -m pip install --upgrade pip```
  ```py -m pip --version```
- Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. Install virtualenv using pip:
  ```py -m pip install --user virtualenv```
- Create a virtual environment:
  ```py -m venv env```
- Activate this project's environment:
  ```.\env\Scripts\activate```
- If you want to deactivate the virtual environment, use:
  ```deactivate```
- Run `python manage.py makemigrations` to identify the changes you have made to the database model.
- Run `python manage.py migrate` to apply migrations.
- To connect database to MySQL Client run command `pip install mysqlclient`
- Start the development server using `python manage.py runserver`.

## Contributors

ISHIKA BANERJEE [@ishika-tia](https://github.com/ishika-tia) </br>
SUDHANSHU RANJAN [@sudhanshuranjan2002](https://github.com/sudhanshuranjan2002) 
