import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

fname = open('data.txt')
lst = list()
count = 0
for i in fname:
    if i.startswith('From'):
        if "From" in i.split():
            print(i.split()[1])
            count += 1
    else:
        continue
print("There were", count, "lines in the file with From as the first word")