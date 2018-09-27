# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:05:31 2018

@author: NI389899
"""

import pandas as pd
from nltk.tokenize import word_tokenize

#Reading csv file using pandas
dataset = pd.read_csv("data_in.csv",encoding = "utf-8")
comments = dataset.loc[: , "Comment"].values

word_tokenize_list = []

for i in comments: 
    word_tokenize_list.append(word_tokenize(i)) #Word Tokenizing

#store in dataframe
pd_frame = pd.DataFrame(word_tokenize_list)

#store in csv
pd_frame.to_csv("data_out.csv")