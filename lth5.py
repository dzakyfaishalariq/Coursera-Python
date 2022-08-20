import os 

os.system('cls')
data = open('data.txt')

for i in data:
    i = i.rstrip()
    if i.startswith('From:'):
        print(i)