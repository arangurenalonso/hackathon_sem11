import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

upload_folder = Path('.') / 'uploads'

db = os.getenv('DATABASE_NAME')
user = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASS')
host = os.getenv('DATABASE_HOST')
port = os.getenv('DATABASE_PORT')


class Config(object):
    SQLALCHEMY_DATABASE_URI = f'postgres://{user}:{password}@{host}:{port}/{db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'pachaqtec'
    UPLOAD_FOLDER = upload_folder


