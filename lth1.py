import os
os.system('cls')
# membuat bilangan ganjil dan genab
array = [1, 19, 20, 41, 5, 6, 7, 8, 10, 11]

genab = []
ganjil = []

# apbaila dikatakan ganji maka x % 2 != 0
# apabila dikatakan genab maka x % 2 == 0
# for i in range(len(array)):
#    if array[i] % 2 == 0:
#        genab.append(array[i])
#    else:
#        ganjil.append(array[i])

for i in array:
    if i % 2 == 0:
        genab.append(i)
    else:
        ganjil.append(i)

print('List Bilangan awal : ')
print(array)
print('bilangan genab : ')
print(genab)
print('bilangan ganjil : ')
print(ganjil)
