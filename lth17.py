# Kripto Moderen
# alat yang  di gunakan
"""
-> ord() -> mengubah ke dalam bentuk desimal
-> bin() -> mengubah ke dalam bentuk Biner
-> hex() -> mengubah ke dalam bentuk heksa

"""


def fungsi(x, key):
    string = ""
    for i in x:
        a = ord(i) ^ ord(key)
        string += chr(a)
    return string


nilai = fungsi("Hallo semuanya apa kabar ayo maling BUKU", "K")
print('ciperteks : {}'.format(nilai))
nilai2 = fungsi(nilai, "K")
print('palintex : {}'.format(nilai2))
