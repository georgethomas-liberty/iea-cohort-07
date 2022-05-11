import operator


def calculate(num1, num2, op="+"):
    if op == "+":
        return operator.add(num1, num2)
        print(calculate)
    if op == "-":
        return operator.sub(num1, num2)
        print(calculate)
    if op == "*":
        return operator.mul(num1, num2)
        print(calculate)
    if op == "/":
        try:
            return operator.truediv(num1, num2)
            print(calculate)
        except ZeroDivisionError:
            print("You cannot divide by zero")
