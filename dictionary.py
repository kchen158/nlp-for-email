import nltk
import string
import re
import numpy as np
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
f = open('ham_training.txt','r')
hamtrain = f.read()
hamtrain = hamtrain.lower()
remove_chars = '[--@_!]'
hamtrain=re.sub(remove_chars,'',hamtrain)
disham_List = nltk.word_tokenize(hamtrain)
stop_words = set(stopwords.words('english'))
train_list = [word for word in disham_List if word not in stop_words]
print(train_list)
print(set(train_list))
print(len(set(train_list)))
print(len(train_list))

'''
freq = nltk.FreqDist(text_list)
for key,val in freq.items():
    print (str(key) + ':' + str(val))
print(len(hamtrain))
print(len(disham_List))
print(len(set(disham_List)))
print(disham_List)

f = open('spam_training.txt','r')
spamtrain = f.read()
spamtrain = spamtrain.lower()
disspam_List = nltk.word_tokenize(spamtrain)
text_list = [word for word in disspam_List if word not in stop_words]
freq = nltk.FreqDist(text_list)
for key,val in freq.items():
    print (str(key) + ':' + str(val))
print(len(spamtrain))
'''

