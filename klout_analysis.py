# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:27:14 2018

@author: Ajay
"""

# Klout score analysis

import pandas as pd
import seaborn as sns


ks = pd.read_csv('kloutscores.csv')
ks.describe() # descrive the stats


# Sample 35 
aSample = ks.sample(35)
aSample.describe()


# Visualize the klout distribution - bimodal distribution
sns.distplot(ks)




