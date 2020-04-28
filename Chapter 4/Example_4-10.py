import os

fp = open('cafe.txt', 'w', encoding='utf_8')
fp

fp.write('café')

fp.close()

os.stat('cafe.txt').st_size

fp2 = open('cafe.txt')
fp2

fp2.encoding

fp2.read()

fp3 = open('cafe.txt', encoding='utf_8')
fp3

fp3.read()

fp4 = open('cafe.txt', 'rb')
fp4

fp4.read()
