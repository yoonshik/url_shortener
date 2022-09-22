Run the following commands to create a local database. You'll need to have mysql/mysqlclient/mariadb set up

```
sudo mysql
CREATE USER 'dbmaster'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON * . * TO 'myusername'@'localhost' WITH GRANT OPTION; 
CREATE DATABASE url_shortener_service_db;
```


Add the following file to the root project directory:

environment
```
export DATABASE_NAME='url_shortener_service_db'
  
export DATABASE_URL='localhost'

export DATABASE_USER='myusername'

export DATABASE_PASSWORD='mypassword'

export DATABASE_PORT='3306'

export NUM_NEW_AVAILABLE_URL_PATHS=10

export DELAY_AVAILABLE_URL_PATH_CHECK_S=10

export MAX_URL_PATH_LENGTH=10
```

Run the following commands to run the server

```
source environment
python manage.py makemigrations
python manage.py migrate
python manage.py runserver