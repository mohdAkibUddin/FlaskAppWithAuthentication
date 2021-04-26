from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

TESTING = True
DEBUG = True
SECRET_KEY = environ.get("SECRET_KEY")
SERVER_NAME = "localhost:5000"
