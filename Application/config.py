SECRET_KEY = "XXXXXXXXXXXXXX"
MYSQL_DATABASE_HOST = "db"
MYSQL_DATABASE_USER = "root"
MYSQL_DATABASE_PASSWORD = "password"
MYSQL_DATABASE_PORT = 3306
MYSQL_DATABASE_DB = "oscarsData"

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')