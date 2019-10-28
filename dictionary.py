import nltk
import string
import re
import pickle
import math
import numpy as np
import types
import pickle
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
# dictionary for ham
'''
f = open('hamtrain.txt','r')
hamtrain = f.read()
hamtrain = hamtrain.lower()
remove_chars = '[--@_!)(,`]'
hamtrain=re.sub(remove_chars,'',hamtrain)
disham_List = nltk.word_tokenize(hamtrain)
stop_words = set(stopwords.words('english'))

train_list = [word for word in disham_List if word not in stop_words]
diction = {}
overall = len(train_list)
nonrepeat = len(set(train_list))
denominator = math.log(overall + nonrepeat)
freq = nltk.FreqDist(train_list)
print(freq.items())
array=np.array(freq.items())
freq_train=array[:,1]
freq_train = map(int, freq_train)
smooth_freq = [i + 1 for i in freq_train]
logfreq = [math.log(i) for i in smooth_freq]
probability = [i - denominator for i in logfreq]
probability = np.array(probability)

probability_single = -denominator
file=open('probability_single.txt','w')
file.write(str(probability_single))
file.close()

np.savetxt("probability.txt",probability)

key_list=array[:,0]
diction=list(key_list)
file = open('dictionary.txt','w')
for i in diction:
    file.write(i)
    file.write('\n')
file.close
'''
# dictionary for the spam

f = open('spamtrain.txt','r')
spamtrain = f.read()
spamtrain = spamtrain.lower()
remove_chars = '[--@_!)(,`]'
spamtrain=re.sub(remove_chars,'',spamtrain)
disspam_List = nltk.word_tokenize(spamtrain)
stop_words = set(stopwords.words('english'))
train_list_spam = [word for word in disspam_List if word not in stop_words]
diction_spam = {}
overall_spam = len(train_list_spam)
nonrepeat_spam = len(set(train_list_spam))
denominator_spam = math.log(overall_spam + nonrepeat_spam)
freqspam = nltk.FreqDist(train_list_spam)
print(freqspam.items())
array=np.array(freqspam.items())
freqspam_train=array[:,1]
freqspam_train = map(int, freqspam_train)
smooth_freqspam = [i + 1 for i in freqspam_train]
logfreqspam = [math.log(i) for i in smooth_freqspam]
probability_spam = [i - denominator_spam for i in logfreqspam]
probability_spam = np.array(probability_spam)

probability_single_spam = -denominator_spam
file=open('probability_single_spam.txt','w')
file.write(str(probability_single_spam))
file.close()

np.savetxt("probability_spam.txt",probability_spam)

spamkey_list=array[:,0]
diction_spam=list(spamkey_list)
file = open('dictionary_spam.txt','w')
for i in diction_spam:
    file.write(i)
    file.write('\n')
file.close




