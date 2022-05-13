import operator
import math


class calc:
    def __init__(self):
        self.total = 0

    def add(self, num1, num2):
        self.total = operator.add(num1, num2)
        return self.total

    def sub(self, num1, num2):
        self.total = operator.sub(num1, num2)
        return self.total

    def mult(self, num1, num2):
        self.total = operator.mul(num1, num2)
        return self.total2

    def div(self, num1, num2):
        self.total = operator.truediv(num1, num2)
        return self.total

    def log(self, num1, num2):
        result = math.log(num1) / math.log(num2)

    def pow(self):
        pass
