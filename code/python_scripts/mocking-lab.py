import os
from unicodedata import name
from unittest.mock import patch


def read_string():
    value = os.getenv("DATABASE_HOST")
    print(value)


read_string()
