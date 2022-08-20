import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

data = open('data.txt')

for i in data:
    i = i.rstrip()
    #print(i.find('From:'))
    if i.find('From:') >= 0:
        print(i)

