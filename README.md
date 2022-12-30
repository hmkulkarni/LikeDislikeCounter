# LikeDislikeCounter

This project is a basic Click counter implemented in Django

**Prerequisite:** Install **Django**: Use command **`pip install Django==3.1.3`**

### Steps to follow to run the code
1. Change the directory to the location where **`manage.py`** file is located.
2. Migrate the models to the database. For this, run the commands in succession
	* **`python manage.py makemigrations`**. This command will prepare your schema.
	* **`python manage.py migrate`**. This command will apply the schema to entire database (**db.sqlite3** file). 
3. Run the command **`python manage.py runserver`**. The default port for Django is **`8000`**, but if for any reason, it is occupied, we can use the command  **`python manage.py runserver <port>`**. replace **\<port\>** with whatever port number you wish to run it in.
4.  If you want to access the database, run the command **`python manage.py createsuperuser`**, and enter the username and password (Password will not be visible while typing). On completing this, type the url **`127.0.0.1:8000/admin`**. This will bring up the django admin panel, which will contain the database. This can be accessed by logging in via the username and password just created. <br>
**NOTE: If the port number is different than 8000, then enter that port number instead in the above url. **
