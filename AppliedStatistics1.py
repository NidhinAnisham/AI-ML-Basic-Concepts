# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:57:49 2018

@author: NI389899
"""

import pandas as pd
import numpy as np
from scipy import stats

#Reading excel file using pandas
dataset = pd.read_excel("Stats.xlsx")

exp_years = dataset.loc[: , "YearsOfExp"].values
salary = dataset.loc[: , "Salary in Rs."].values

#Getting mean,mode,median using numpy in-built functions
mean_exp = np.mean(exp_years)
mean_sal = np.mean(salary)
mode_exp = stats.mode(exp_years)
mode_sal = stats.mode(salary)
median_exp = np.median(exp_years)
median_sal = np.median(salary)

#Printing obtained values
print("Mean Years Of Experience: ",mean_exp)
print("Mean Salary: ",mean_sal)
print("Mode Years Of Experience: ",mode_exp[0][0])
print("Mode Salary: ",mode_sal[0][0])
print("Median Years Of Experience: ",median_exp)
print("Median Salary: ",median_sal)