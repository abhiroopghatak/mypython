#!/usr/bin/env python
# coding: utf-8
# Maintained by : Abhiroop Ghatak <ghatak.20@gmail.com>
'''Conceptually, we think of the whole document as a “bag” of words, rather than a sequence. We represent the document simply by the frequency of each word. For example,
if we have a vocabulary of 1,000 words, then the whole document will be represented by a 1,000-dimensional vector,
where the vector’s ith entry represents the frequency of the ith vocabulary word in the document.'''


import pandas as pd
import numpy as np
import nltk
import re
import heapq 

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("stopwords")
from nltk.stem import PorterStemmer

stemmer=PorterStemmer()



def preprocess(corpus):
    ## getting list of sentences from paragraph/corpus
    sentences=nltk.sent_tokenize(corpus)
    
    for i in range(len(sentences)):
        ##Removing all other characters and replace them with space which arent alphabets
        sentences[i]=re.sub('[^a-zA-Z]', ' ' ,  sentences[i])
        ##Getting list of words from each sentences and converting all to lower case
        words=nltk.word_tokenize(sentences[i].lower())
        ##Removing all stop words then apply stemmimg to have the root word
        words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
        ##setting sentence[i] by joining these processed individual words and joining them by empty space
        sentences[i]=' '.join(words) #converting all words in same sequence to a sentences
    ##Returning final preprocessed list of sentences    
    return sentences
## create a dictionary with different words and its occurances in our refined text

def getWordCountDictionary(sentences):
    print(f"number of sentence in argument list are {len(sentences)}")
    #declared an empty dictionary
    word2count = {} 
    ## Traverse for each sentences in the list
    for i in range(len(sentences)):
        ##Get list of words
        words = nltk.word_tokenize(sentences[i]) 
        ##for every new word insert entry to dictionary and adding occurances for every repeating word
        for word in words: 
            if word not in word2count.keys(): 
                word2count[word] = 1
            else: 
                word2count[word] += 1
    return word2count


##Build Bag of Words Model

def get_bow(sentences,freq_words):
    X = [] 
    for data in sentences: 
        vector = [] 
        for word in freq_words: 
            if word in nltk.word_tokenize(data): 
                vector.append(1) 
            else: 
                vector.append(0) 
        X.append(vector) 
    X = np.asarray(X) 
    return X
    
##-----------------
corpus='''Beans. I was trying to explain to somebody as we were flying in, that’s corn.  That’s beans. And they were very impressed at my agricultural knowledge. Please give it up for Amaury once again for that outstanding introduction. I have a bunch of good friends here today, including somebody who I served with, who is one of the finest senators in the country, and we’re lucky to have him, your Senator, Dick Durbin is here. I also noticed, by the way, former Governor Edgar here, who I haven’t seen in a long time, and somehow he has not aged and I have. And it’s great to see you, Governor. I want to thank President Killeen and everybody at the U of I System for making it possible for me to be here today. And I am deeply honored at the Paul Douglas Award that is being given to me. He is somebody who set the path for so much outstanding public service here in Illinois. Now, I want to start by addressing the elephant in the room. I know people are still wondering why I didn’t speak at the commencement.'''


# In[28]:


sentences=preprocess(corpus)
print(sentences)
print(sentences)
word_count_dict=getWordCountDictionary(sentences)
print(word_count_dict)
print(f"----------number of words in dict are {len(word_count_dict)}")

freq_words = heapq.nlargest(30, word_count_dict, key=word_count_dict.get)
print(f"----------number of words in freq_words are {len(freq_words)}")


## Get Bow Model

x=get_bow(sentences,freq_words)
print(f"----------number of words in bow-X are {len(x)}")
print(x)

##--------------END------

