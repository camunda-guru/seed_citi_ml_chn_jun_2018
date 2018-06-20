# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:31:03 2018

@author: Balasubramaniam
"""
import pandas as pd
#df2=pd.read_csv("https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv")
#print(df2)
df3=pd.read_csv("https://raw.githubusercontent.com/eswaribala/seed_citi_ml_chn_jun_2018/master/diabetes.csv")
print(df3)
df1=pd.read_excel("F:/citi_ml_jun2018/day2/statistics/alcholconsumption_new.xlsx")
print(df1)
df = pd.read_csv("Data.csv")
print ("Dataframe", df)
print ("Shape", df.shape)
print ("Length", len(df))
print ("Column Headers", df.columns)
print ("Data types", df.dtypes)
print("Index", df.index)
print ("Values", df.values)
print(df.head(2))
print(df.tail(2))

    
#slicing
    
print(df['Age'])    
# select rows 0,1,2 (but not 3)
print(df[0:3])
# select the last element in the list
print(df[-1:])

#loc: indexing via labels or integers
#iloc: indexing via integers


# select all columns for rows of index values 0 and 8
#will check
print(df.loc[[0, 8], :])#only 0 and 8th row
print(df.iloc[:,0]) # first column of data frame (first_name))
print(df.iloc[:, 0:2])#first 2 columns
print(df.iloc[[0,3,6], [0,2]])#0th, 3rd, 6th row + 1st and 2nd columns.

from numpy.random import seed
from numpy.random import rand

seed(42)
df = pd.DataFrame({'Weather' : ['cold', 'hot', 'cold', 'hot',
'cold', 'hot', 'cold'],
'Food' : ['soup', 'soup', 'icecream', 'chocolate',
'icecream', 'icecream', 'soup'],
'Price' : 10 * rand(7)})
print (df)

weather_group = df.groupby('Weather')
i = 0
for name, group in weather_group:
    i = i + 1
    print ("Group", i, name)
    print (group)
    
