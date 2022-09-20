import urllib.request as gett
import urllib.parse as par
import urllib.error as err
from bs4 import BeautifulSoup as ber

# url = input('url : ')
html = gett.urlopen('http://www.dr-chuck.com/page1.htm').read()
soup = ber(html, 'html.parser')

tags = soup('a')

print(soup)
for i in tags:
    print(i)
    print(i.get('href', None))
