from ast import Break, Continue
import inquirer, os, sys, re
from pprint import pprint
from inquirer import errors

fruits = [
    "Apple",
    "Watermelon",
    "Orange",
    "Pear",
    "Cherry",
    "Strawberry",
    "Nectarine",
    "Grape",
    "Mango",
    "Blueberry",
    "Pomegranate",
]
vegetables = [
    "Carrot",
    "Brussels sprout",
    "Pumpkin",
    "Cabbage",
    "Potato",
    "Eggplant",
    "Sweet potato",
    "Turnip",
    "Green chilli",
    "Onion",
    "Lettuce",
    "Radish",
]

questions = [
    inquirer.List(
        "size",
        message="What would you like to do?",
        choices=[
            "Display both lists",
            "Add a fruit",
            "Add a vegetable",
            "Remove a fruit",
            "Remove a vegetable",
            "Reverse list of fruits",
            "Reverse list of vegetables",
            "Quit",
        ],
    ),
]

# answers = inquirer.prompt(questions)

while answers["size"] != "Quit":
    answers = inquirer.prompt(questions)
    if answers["size"] == "Display both lists":
        print(f"List of Fruits\n {fruits}")
        print(f"List of vegetables\n {vegetables}")

    elif answers["size"] == "Add a fruit":
        Add_fruit = input("Please enter a fruit you would like added to the list. ")
        fruits.append(Add_fruit)
        print(f"List of Fruits\n {fruits}")

    elif answers["size"] == "Add a vegetable":
        Add_veg = input("Please enter a vegetables you would like added to the list. ")
        vegetables.append(Add_veg)
        print(f"List of vegetables\n {vegetables}")

    elif answers["size"] == "Remove a fruit":
        fruits.sort()
        print(f"List of Fruits\n {fruits}")
        Rem_fruit = input("Please enter a fruit you would like removed from the list. ")
        fruits.remove(Rem_fruit)
        print(f"List of Fruits\n {fruits}")

    elif answers["size"] == "Remove a vegetable":
        vegetables.sort()
        print(f"List of vegetables\n {vegetables}")
        Rem_veg = input(
            "Please enter a vegetables you would like removed from the list. "
        )
        vegetables.remove(Rem_veg)
        print(f"List of vegetables\n {vegetables}")

    elif answers["size"] == "Reverse list of fruits":
        print(f"List of Fruits in Reverse\n {fruits[::-1]}")

    elif answers["size"] == "Reverse list of vegetables":
        print(f"List of Fruits in Reverse\n {vegetables[::-1]}")

    elif answers["size"] == "Quit":
        break
