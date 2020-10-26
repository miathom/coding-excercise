# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# Desired Output:
# cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

senderList = list()
senderDict = dict()
user = None
max = None

for line in handle:
    line = line.strip()
    if len(line) < 2 or not line.startswith("From "):
        continue
    tmpList = line.split()
    senderList.append(tmpList[1])
    
for sender in senderList:
    senderDict[sender] = senderDict.get(sender,0) + 1
    
#print(senderDict)
    
for sender,count in senderDict.items():
    if max is None or count > max:
        user = sender
        max = count
     
print(user, max)
