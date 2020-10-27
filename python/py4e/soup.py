# Write a program that read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos = 18
count = 7
name = None

def open(u):
    html = urlopen(u, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup 

while count > 0:
    soup = open(url)
    tags = soup('a')
    
    n = 1

    for tag in tags:
        if n > pos: break
        url = tag.get('href', None)
        name = tag.contents[0]
        n = n + 1

    count = count - 1

print(name)





    
    




