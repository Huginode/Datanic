import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import Data
data = pd.read_excel('titanic3.xls')

# Remove all data that isn't needed
data = data.drop(['name', 'sibsp', 'parch','embarked', 'ticket', 'fare', 'cabin', 'boat', 'body', 'home.dest'], axis = 1)

# Clean data by removing passengers with unkwon age
data = data.dropna(axis=0)

# Grouping passengers by sex and class
a = data.groupby(['sex', 'pclass']).mean()
print(a)
