#!/usr/bin/env python
# coding: utf-8
#@author: Abhiroop Ghatak

import pandas as pd
import numpy as np
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

corpus="""My dearest, From the moment we met, my heart has known only you. Your laughter is my favorite melody 10 on 10, and your smile lights up even the darkest days. Every second spent with you feels like a beautiful dream, and I never want to wake up. With you by my side, the world feels like a kinder, warmer place.

You have taught me the true meaning of love, and I am forever grateful for your presence in my life. I cherish every little moment we share and look forward to a future filled with more love, laughter, and adventure.

You are my heart’s forever home.

Yours always,"""

def get_pre_processed_sentence_list(corpus):
    sentences=sent_tokenize(corpus)
    sentences = [remove_punctuation(sentence) for sentence in sentences]
    return sentences
    
def remove_punctuation(sentence):
    sentence=sentence.lower()
    words=word_tokenize(sentence)
    words = [item.replace(",", "") for item in words]
    words = [item.replace(".", "") for item in words]
    sentences=' '.join(words)
    # Using filter() and lambda function to filter out punctuation and number characters
    result = ''.join(filter(lambda x: x.isalpha() or x.isspace(), sentence))
    #print('----',result)
    return result


def get_total_number_of_words_post_cleaning(sentences):
    word_count=0
    for sentence in sentences:
        words=sentence.split(' ')
        word_count=word_count+len(words)
    return word_count
    
def get_unique_word_set(sentences):
    set_of_words=set()
    for sentence in sentences:
        words=sentence.split(' ')
        set_of_words = set_of_words.union(set(words))
        while("" in set_of_words):
            set_of_words.remove("")
    return set_of_words

def word_occurance_in_sentence(word,sentence):
    # split the string by spaces in a
    a = sentence.split(" ")
    # search for pattern in a
    count = 0
    for i in range(0, len(a)):
        # if match found increase count 
        if (word == a[i]):
           count = count + 1
    return count
def get_tf(words_set,sentences):
    word_list=list(words_set)
    df_tf = pd.DataFrame(np.zeros((no_of_sentences, len(words_set))), columns=word_list)
    #df_tf = pd.DataFrame(np.zeros(( len(words_set),no_of_sentences)),index=list(words_set))
    #print(df_tf)
    ## word occurance in given corpus
    # Create an empty dictionary 

    for i in range(len(sentences)):
        print(sentences[i])
        for j in range(len(word_list)):
            #print(w[j])
            #print(sentences[i])
            word_frequency_in_sentence=word_occurance_in_sentence(word_list[j],sentences[i])
            #print(f'word and its word_frequency_in_sentence= {word_list[j]} , {word_frequency_in_sentence}')
            #print(f'num of words in the sentence ={len(sentences[i].split())}')
            x=word_frequency_in_sentence/len(sentences[i].split())
            #print(x)
            df_tf.iloc[i][word_list[j]]=x
    return df_tf

def get_idf(words_set,sentences):
    word_list=list(words_set)
    idf={} #empty dict declaration 
    total_sentences=len(sentences)
    for w in word_list:
        k=0 # no of sentences that contain this word
        for i in range(total_sentences):
            k=word_occurance_in_sentence(w,sentences[i])
        k+=1
        idf[w]=(np.log10(total_sentences/k)).item()
    return idf

def get_tf_idf(df_tf,idf):
    df_tf_idf = df_tf.copy()
    for w in words_set:
        for i in range(no_of_sentences):
            df_tf_idf[w][i] = df_tf[w][i] * idf[w]
        
    return df_tf_idf

##-------------------functions ends -------------------


sentences=get_pre_processed_sentence_list(corpus)

no_of_sentences=len(sentences)
words_set=get_unique_word_set(sentences)
total_words=get_total_number_of_words_post_cleaning(sentences)
print('Number of sentences: ', no_of_sentences)
print('Number of words in the corpus post_cleaning:',total_words)
print('Number of Unique words: ', len(words_set))
print('The words in the corpus: \n', words_set)
##TF
df_tf=get_tf(words_set,sentences)
print(df_tf)

##IDF
idf = get_idf(words_set,sentences)       
print(f'IDF={idf}')         

##tf-idf
print('-------------df_tf_idf-------------')
df_tf_idf=get_tf_idf(df_tf,idf )
print(df_tf_idf)

