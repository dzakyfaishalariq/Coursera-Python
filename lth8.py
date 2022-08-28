import re

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


def analisis(data='', jumlah=0):
    if data != '':
        data = open(data)
        for i in data:
            i = i.rstrip()
            r = re.findall('[a-z0-9]+', i)
            if r != []:
                for k in r:
                    print(k)

        print()
        print("----------data berhasil di eksekusi------------")
        print("Jumlah nya : {}".format(jumlah))
    else:
        print('Data kosong atau salah input')


name_data = input('> masukan data : ')
analisis(name_data)
