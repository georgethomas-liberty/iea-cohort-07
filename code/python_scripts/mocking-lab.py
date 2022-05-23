import os
from unicodedata import name


def read_string(your_string):
    value = os.getenv("DATABASE_HOST", your_string)
    print(value)


# os.getenv
# testname = os.getenv("DATABASE_HOST", "localhost")
# print(testname)

read_string()
