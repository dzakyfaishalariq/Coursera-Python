import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter : ')
count = int(input('Enter count : '))
position = int(input('Enter position : '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# array = []
tags = soup('a')
# for tag in tags:
#     # print(tag.get('href', None))
#     h = tag.get('href', None).split('/' or '.')
#     h = h[3].split('_')[2].split('.')[0]
#     array.append(h)
print("Retrieving: {}".format(url))
for i in range(count):
    nilai = tags[position-1].get('href', None)
    print("Retrieving: {}".format(nilai))
    html = urllib.request.urlopen(nilai, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
print('The answer to the assignment for this execution is {}'.format(nilai.split('_')[2].split('.')[0]))
 