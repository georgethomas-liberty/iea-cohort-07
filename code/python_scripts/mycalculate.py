#!/usr/bin/env python3
import operator
import math


def calculate(num1, num2, op):
    if op == "+":
        return operator.add(num1, num2)

    if op == "-":
        return operator.sub(num1, num2)

    if op == "*":
        return operator.mul(num1, num2)

    if op == "/":
        try:
            return operator.truediv(num1, num2)
        except ZeroDivisionError:
            print("You cannot divide by zero")

    if op == "log":
        try:
            result = math.log(num1) / math.log(num2)
        except ValueError:
            print("Cannot take log of 0!")
            return None
        except ZeroDivisionError:
            print("Cannot take log base 1!")
            return None
        else:
            return result
