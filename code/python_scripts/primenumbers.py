lower = int(input("Please enter a number to start with: "))
upper = int(input("Please enter a higher number to end with: "))

if lower >= upper:
    upper = int(input("Please enter a higher number to end with: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("{:4d}".format(num), end=" ")
