import os
import os.path
import nltk
from nltk.tokenize import sent_tokenize
filedirham='/Users/kejunchen/Desktop/hamdebug/'
filenames=os.listdir(filedirham)
file=open('ham_training.txt','w')
for filename in filenames:
    filepath=filedirham+filename
    f = open(filepath, 'r')
    for line in open(filepath):
        file.writelines(line)
    file.write('\n')
file.close
file=open('spam_training.txt','w')
filedirspam='/Users/kejunchen/Desktop/spamdebug/'
filenames=os.listdir(filedirspam)
for filename in filenames:
    filepath=filedirspam+filename
    f = open(filepath, 'r')
    for line in open(filepath):
        file.writelines(line)
    file.write('\n')
file.close
