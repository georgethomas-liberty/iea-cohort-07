"""
x = 5
y = 6
sum = x * y
print(sum)


roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
print(roman.keys())
"""

"""
def print_name(name):
    print(name)


print_name("george")


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes", mname="thomas")


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)
"""


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(4)


import string
string.

import random
random.

