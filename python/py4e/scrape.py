# Write a program to read the HTML file and parse the data, extracting numbers and compute the sum of the numbers in the file. 
# use urllib and beautifulsoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
numberList = list()
line = soup('span')

for each in line:
    number = each.contents[0]
    numberList.append(number)

for number in numberList:
    sum += int(number)

print(sum)

