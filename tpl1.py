import os


class warna:
    merah = '\033[31m'
    kuning = '\033[33m'
    normal = '\033[0m'


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

name = input('>')
handel = open(name)
lis = []
lis2 = {}
lis3 = []
for i in handel:
    if i.startswith('From') and not(i.startswith('From:')):
        lis.append(i.split()[5].split(':')[0])

for i in sorted(lis):
    lis2[i] = lis2.get(i, 0) + 1

for x, y in lis2.items():
    lis3.append((x, y))
print(warna.merah +'Daftar email yang paling banyak dikirimkan' + warna.normal)
for i, j in lis3:
    print(i, j)
# cetak ke file txt
tulis = open('tulis.txt', 'w')
tulis.write(">>Ini merupakan hasil jawaban<<" + '\n')
for i, j in lis3:
    tulis.write(i + ' ' + str(j) + '\n')
tulis.close()
# buka file txt secara langsun melalui os
os.system('tulis.txt')
