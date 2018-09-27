# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:42:49 2018

@author: NI389899
"""
from nltk.tokenize import word_tokenize

#Calculating Sentiment for each line
def sentiment(text):
    sent_words = word_tokenize(text)
    positive_vocab = ["nice","excellent","good","wonderful","best","better","awesome",
                  "beautiful","beauty","beautifully","supreme"]
    negative_vocab = ["hate","hatred","annoyed","annoy","annoyingly","nasty"]
    p_count = 0
    n_count = 0
    for word in sent_words:
        for i in positive_vocab:
            if word == i:
                p_count += 1
        for i in negative_vocab:
            if word == i:
                n_count += 1
    if(p_count>n_count):
        return("Positive")
    elif(p_count<n_count):
        return("Negative")
    else:
        return("Neutral")
        
comments = []

#Reading txt file
with open("NLP5.txt") as f:
    for line in f:
        comments.append(line)

#Calculating overall sentiment
pos = 0
neg = 0
for i in comments:
    sen = sentiment(i)
    if(sen == "Positive"):
        pos += 1
    elif(sen == "Negative"):
        neg += 1
    print(i," : ",sen,"\n")

if(pos > neg):
    print("Overall Sentiment: Positive")
elif(neg>pos):
    print("Overall Sentiment: Negative")
else:
    print("Overall Sentiment: Neutral")
