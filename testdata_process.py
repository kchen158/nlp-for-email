import os
import os.path
import nltk
import string
import re
import math
import numpy as np
import types
import sys
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

datalist = []
datapath = []
diction = []
transform = []
filepath='/Users/kejunchen/Desktop/testdebugham/'
filenames=os.listdir(filepath)

# ignore the ds.store folder
for i in filenames:
    if os.path.splitext(i)[1] == '.txt':
        datalist.append(i)
for text_file in datalist:
        datapath.append(filepath+text_file)
allposterior_ham = [0 for i in range(len(datapath))]
# import dictionary and probability
with open("dictionary.txt",'r') as f:
    for line in f:
        transform.append(list(line.strip('\n').split(',')))
for item in transform:
    for it in item:
        diction.append(it)
probability = np.loadtxt("probability.txt", delimiter=',')
probability_single=open("probability_single.txt",'r').read()

k = int(0)
for filename in datapath:
    try:
        f = open(filename, 'r')
        hamtest = f.read()
    finally:
        if f:
            f.close()
    hamtest = hamtest.lower()
    remove_chars = '[--@_!)(,`]'
    hamtest = re.sub(remove_chars, '', hamtest)
    hamtest_list = nltk.word_tokenize(hamtest)
    stop_words = set(stopwords.words('english'))
    test_list = [word for word in hamtest_list if word not in stop_words]
    freq = nltk.FreqDist(test_list)
    array = np.array(freq.items())
    freq_test = array[:, 1]
    freq_test = map(int,freq_test)
    key_list = list(array[:, 0])
    notinclass = [i for i in key_list if i not in diction]
    inclass = [i for i in key_list if i in diction]
    single_number = len(notinclass)
    single_probability= single_number * float(probability_single)
    m = int (-1)
    posterior = single_probability
    for feature in inclass:
        m = m + 1
        place = diction.index(feature)
        freqency = probability[place]
        repeat = freq_test[m]
        posterior_ham = posterior + freqency * repeat
    allposterior_ham [k] = posterior_ham
    k = k + 1
print(allposterior_ham)



# spam situation


datalist = []
datapath = []
diction_spam = []
transform_spam = []
filepath='/Users/kejunchen/Desktop/testdebugham/'
filenames=os.listdir(filepath)

# ignore the ds.store folder
for i in filenames:
    if os.path.splitext(i)[1] == '.txt':
        datalist.append(i)
for text_file in datalist:
        datapath.append(filepath+text_file)
allposterior_spam = [0 for i in range(len(datapath))]
# import dictionary_spam and probability_spam
with open("dictionary_spam.txt",'r') as f:
    for line in f:
        transform_spam.append(list(line.strip('\n').split(',')))
for item in transform_spam:
    for it in item:
        diction_spam.append(it)
probability_spam = np.loadtxt("probability_spam.txt", delimiter=',')
probability_single_spam=open("probability_single_spam.txt",'r').read()

k = int(0)
for filename in datapath:
    try:
        f = open(filename, 'r')
        spamtest = f.read()
    finally:
        if f:
            f.close()
    spamtest = spamtest.lower()
    remove_chars = '[--@_!)(,`]'
    spamtest = re.sub(remove_chars, '', spamtest)
    spamtest_list = nltk.word_tokenize(spamtest)
    stop_words = set(stopwords.words('english'))
    test_list_spam = [word for word in spamtest_list if word not in stop_words]
    freq_spam = nltk.FreqDist(test_list_spam)
    array = np.array(freq_spam.items())
    freq_test_spam = array[:, 1]
    freq_test_spam = map(int,freq_test_spam)
    key_list_spam = list(array[:, 0])
    notinclass_spam = [i for i in key_list_spam if i not in diction_spam]
    inclass = [i for i in key_list_spam if i in diction_spam]
    single_number_spam = len(notinclass_spam)
    single_probability_spam= single_number_spam * float(probability_single_spam)
    m = int (-1)
    posterior_spam = single_probability_spam
    for feature in inclass:
        m = m + 1
        place = diction_spam.index(feature)
        freqency_spam = probability_spam[place]
        repeat_spam = freq_test_spam[m]
        posterior_spam = posterior_spam + freqency_spam * repeat_spam
    allposterior_spam[k] = posterior_spam
    k = k + 1
print(allposterior_spam)


