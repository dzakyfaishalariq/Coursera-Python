# menggunakan search
import re
import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

data = open('data.txt')

# re.search -> mencari kata yang berada di dalam kalimat
for i in data:
    i = i.rstrip()
    if re.search('From:',i):
        print(i)