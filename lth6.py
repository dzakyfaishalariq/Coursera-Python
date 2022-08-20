import os
import re
os.system("cls")

# penggunaan findall
string = "Hallo 20 dan 0.59 saya merupakan 30 nya dari 4 untuk melakukan 50 jambu"

# output = re.findall('[0-9]+', string) -> berkaitan ke angka yang di dapat
# berkaitan ke fariabel huruf yang dibentuk
output = re.findall('[aiueo]+', string)
# melakukan pemilahan angka atau bilangan integer dari string
print(output)
