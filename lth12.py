# print(ord('A')) -> mencari lokasi ASCII
import urllib.request as get
import urllib.parse as par
import urllib.error as err
# ambil tulisan dengan reques
data = get.urlopen('http://data.pr4e.org/romeo.txt')

data_ditc = {}
for i in data:
    i = i.decode().split()
    for j in i:
        data_ditc[j] = data_ditc.get(j, 0) + 1

for i, j in data_ditc.items():
    print(i, j)
