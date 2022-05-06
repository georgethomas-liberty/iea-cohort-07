import os
import random

path = "code/python_scripts/"

choosefile = []
for txtfiles in os.listdir(path):
    if txtfiles.endswith(".txt"):
        choosefile.append(txtfiles)
print(choosefile)

infilename = str(input("Please enter a File Name.: "))
fileread = open(os.path.join(path, infilename), "r")


outfilename = str(random.randrange(1, 9)) + infilename
filewrite = os.path.join(path, outfilename)

with open(filewrite, "w") as outfile:

    for line in infilename:
        outfile.write(line + "\n")

fileread.close()
