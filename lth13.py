# mencetak tulisan website
import re
import urllib.request as get
import urllib.parse as par
import urllib.error as err

data = get.urlopen('http://www.dr-chuck.com/page1.htm')

for i in data:
    i = i.decode().rstrip()