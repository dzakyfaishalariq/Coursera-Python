from cgi import print_environ
import os
import re

os.system('cls')

string = 'Apa nama mu : nama saya Dzaky kamu : akan kah hidup : dia adalah Dzaky dzaky@gmail.com ini wajib!!'

output = re.findall('^Apa.+:', string)
output2 = re.findall('^A.+?:', string)
output3 = re.findall('\S+!\S+', string)
output4 = re.findall('\S+?@\S+', string)
output5 = re.findall('@([^ ]*)', string)
fin = string.find('@')
fin2 = string.find(' ', fin)
print(fin)
print(fin2)
print(string[fin+1:fin2])
print(output5)
print(output)
print(output2)
print(output3)
print(output4)
