import sys
import mycalculate

mycalculate.calculate

if len(sys.argv) < 4:
    exit("Usage: " + sys.argv[0] + " OPERAND OPERAND OPERATOR")

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
op = sys.argv[3]

answer = calculate(num1, num2, op)

print(answer)
# print(sys.argv[1:])
