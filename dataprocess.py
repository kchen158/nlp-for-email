import os
import os.path
import nltk
# combine the training ham data into one .txt file
filepath='/Users/kejunchen/Desktop/hamdebug/'
filenames=os.listdir(filepath)
datalist = []
datapath = []
for i in filenames:
    if os.path.splitext(i)[1] == '.txt':
        datalist.append(i)
for text_file in datalist:
        datapath.append(filepath+text_file)
with open('hamtrain.txt', 'w') as fh:
    for text_file in datapath:
        data = open(text_file, 'r')
        fh.write(data.read())
fh.close()

# combine the training spam data into one .txt file
filepath='/Users/kejunchen/Desktop/spamdebug/'
filenames=os.listdir(filepath)
datalist = []
datapath = []
for i in filenames:
    if os.path.splitext(i)[1] == '.txt':
        datalist.append(i)
for text_file in datalist:
        datapath.append(filepath+text_file)
with open('spamtrain.txt', 'w') as fh:
    for text_file in datapath:
        data = open(text_file, 'r')
        fh.write(data.read())
fh.close()

with open('train.txt','w') as fh:
    data = open("hamtrain.txt",'r')
    fh.write(data.read())
    data = open("spamtrain.txt", 'r')
    fh.write(data.read())
