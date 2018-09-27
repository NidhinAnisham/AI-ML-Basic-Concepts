# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:26:01 2018

@author: NI389899
"""

import pandas as pd
import numpy as np

#Reading excel file using pandas
dataset = pd.read_excel("Stats.xlsx")

exp_years = dataset.loc[: , "YearsOfExp"].values
salary = dataset.loc[: , "Salary in Rs."].values

#Getting standard deviation,variance using numpy in-built functions
std_exp = np.std(exp_years)
std_sal = np.std(salary)
var_exp = np.var(exp_years)
var_sal = np.var(salary)

#Printing obtained values
print("Standard-Deviation Years Of Experience: ",std_exp)
print("Standard-Deviation Salary: ",std_sal)
print("Variance Years Of Experience: ",var_exp)
print("Variance Salary: ",var_sal)