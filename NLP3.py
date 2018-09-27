# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:36:43 2018

@author: NI389899
"""
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import chunk
from nltk import tag

comments = []

#Reading txt file
with open("data.txt") as f:
    for line in f:
        comments.append(line)

sent_tokenize_list = []
sent_chunk = []

for i in comments:
    sent_tokenize_list.append(sent_tokenize(i)) #sentence tokenization 
    chunks = chunk.ne_chunk(tag.pos_tag(word_tokenize(i)))
    chunks.draw() #draw tree structure
    sent_chunk.append(chunks) #NE Chunking after POS Tagging
