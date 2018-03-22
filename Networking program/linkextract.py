#Parsing HTML using regular expressions
# Search for lines that start with From and have an at sign
import urllib.request, urllib.parse, urllib.error
import re

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
#The findall regular expression method will give us a list of all of the strings that match our regular expression, returning only the link text between the double quotes.
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())