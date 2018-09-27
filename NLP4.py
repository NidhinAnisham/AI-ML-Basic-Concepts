# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:34:30 2018

@author: NI389899
"""
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer

comments = []

#Reading txt file
with open("data.txt") as f:
    for line in f:
        comments.append(line)

lem_comments = []
stem_comments = []

#Initializing stopwords set
stop = set(stopwords.words('english'))

#Initializing lemmatizer
lemma = WordNetLemmatizer()

#Initializing stemmer
stemmer = SnowballStemmer("english")

for doc in comments:
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop]) #removing stopwords
    normalized = " ".join(lemma.lemmatize(word) for word in stop_free.split()) #lemmatizing
    stemmed = " ".join(stemmer.stem(word) for word in stop_free.split()) #stemming
    lem_comments.append(normalized)
    stem_comments.append(stemmed)

print(lem_comments) #printing lemmatized results
print(stem_comments) #printing stemmed results