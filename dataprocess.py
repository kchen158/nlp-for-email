import os
import os.path

filedirham='/Users/kejunchen/Desktop/hamdebug/'
filenames=os.listdir(filedirham)
for filename in filenames:
    f = open(filedirham+filename, 'r')
    print(f.read())

filedirspam='/Users/kejunchen/Desktop/spamdebug/'
filenames=os.listdir(filedirspam)
for filename in filenames:
    f = open(filedirspam+filename, 'r')
    print(f.read())


