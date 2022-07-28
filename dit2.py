import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

filname = input('Masukan file >')
fl = open(filname)
data = {}
for i in fl:
    if i.startswith('From:'):
        key = i.rstrip().split()[1]
        data[key] = data.get(key, 0) + 1
value = []
for i in data.values():
    value.append(i)
for i, z in data.items():
    if data[i] == max(value):
        print(i, z)
