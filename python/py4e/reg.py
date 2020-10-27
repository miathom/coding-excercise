# Read a file and find all the numbers
# print out the sum.

import re
filename = input("Enter the filename:")
file = open(filename)

sum = 0
numberList = list()

for line in file:
    numberList += re.findall('([0-9]+)', line)

for number in numberList:
    sum += int(number)

print(sum)



