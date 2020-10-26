# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# Desired Output:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

timeList = list()
hrList = list()
hrDict = dict()

for line in handle:
    line = line.strip()
    if len(line) < 6 or not line.startswith("From "):
        continue
    tmpList = line.split()
    timeList.append(tmpList[5])
    
for time in timeList:
    tmpList = time.split(":")
    hrList.append(tmpList[0])
    
for hour in hrList:
    hrDict[hour] = hrDict.get(hour,0) + 1
    
countList = sorted([(k,v) for (k,v) in hrDict.items()])

for k,v in countList:
    print(k,v)