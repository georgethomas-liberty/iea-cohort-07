"""
x = 7
y = 6
sum = x * y
print(sum)


man = "george"
print(man)


age = int(0x2B)
print("JR is", age)
"""
"""
list = [1, 2, 3, 4, 5]
list.append(7)
list.insert(0, 8)
list.insert(2, "george")
list.extend([58, "Geeks", "Always"])
print(list)
# print(list[3:5])
# print(len(list))
list.reverse()

print(list)
"""

# print(2 + 3 == 6)

# import __future__
import calendar
import datetime
import math


string = 0
while len(str(string)) != 5:
    string = input("enter a 5-letter string: ")
    print(f"{string} is not 5 letters ")
else:
    print(f"{string} is 5 letters ")
