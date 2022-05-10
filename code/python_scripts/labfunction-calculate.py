def calculate(num1, num2, op="+"):
    if op == "+":
        return num1 + num2
        print(calculate)
    if op == "-":
        return num1 - num2
        print(calculate)
    if op == "*":
        return num1 * num2
        print(calculate)
    if op == "/":
        try:
            num2 != 0
            return num1 / num2
            print(calculate)
        except ZeroDivisionError:
            print("You cannot divide by zero")
