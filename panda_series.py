import pandas as pd
import numpy as np

#1. Create Panda Series using list

my_data = [10,20,30,40,50]
my_labels = ['a', 'b', 'c', 'd', 'e']

print ( f"Panda Series using default index:\n{pd.Series (data=my_data)}" )
print ( f"Panda Series using labels index:\n{pd.Series (data=my_data, index=my_labels)}")

#2. Create Panda Series using dictionary

my_dict ={'a':100, 'b':200, 'c':300}

print ( f"Panda Series using dictinary:\n{pd.Series (data=my_dict) }" )
