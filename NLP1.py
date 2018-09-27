# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:31:58 2018

@author: NI389899
"""

import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import chunk
from nltk import tag

#Reading csv file using pandas
dataset = pd.read_csv("data_in.csv",encoding = "utf-8")
comments = dataset.loc[: , "Comment"].values

sent_tokenize_list = []
word_tokenize_list = []
sent_chunk = []

for i in comments:
    sent_tokenize_list.append(sent_tokenize(i)) #sentence tokenization   
    sent_chunk.append(chunk.ne_chunk(tag.pos_tag(word_tokenize(i)))) #NE Chunking after POS Tagging

print(sent_chunk)

#store in dataframe
pd_frame = pd.DataFrame(sent_tokenize_list)

#store in csv
pd_frame.to_csv("data_out.csv")
