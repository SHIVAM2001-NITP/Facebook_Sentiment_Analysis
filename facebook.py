# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:38:06 2021

@author: SHIVAM KUMAR
"""

import pandas as pd  # import the pandas module for reading the excel sheet and
import nltk   # import nltk-module=natural language toolkit
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')
file = "data_file.xlsx"

dfs = pd.read_excel(open('data_file.xlsx', 'rb'), sheet_name='Sheet1')  # reading and parsing excel sheet to data frames

dfs = list(dfs['Timeline'])  # removes the blank columns from the dataframes
print(dfs)
sentiment_intensity_analyser=SentimentIntensityAnalyzer()
str1 = "UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if a == -1:
        ss = sentiment_intensity_analyser.polarity_scores(data)
        print(data)
        for k in ss:
            print(k, ss[k])
