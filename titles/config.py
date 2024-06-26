import os
from os.path import join, dirname
from dotenv import load_dotenv


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


DATABASE_URL = get_from_env("DATABASE_URL")
