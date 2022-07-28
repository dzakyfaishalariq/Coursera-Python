import os
import numpy as np
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
fname = input("> ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip().split(' ')
    for i in line:
        if i in lst:
            continue
        lst.append(i)

print("=================")
print(sorted(lst))
