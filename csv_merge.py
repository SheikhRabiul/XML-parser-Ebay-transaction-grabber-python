# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:23:41 2017

@author: Sheikh Rabiul Islam
"""
import pandas as pd
import glob

csv_files = glob.glob("*.csv")
data_list = []

for fname in csv_files:
    print("processing started : %s",fname)
    data_list.append(pd.read_csv(fname,encoding='latin-1'))
    print("processing ended : %s",fname)
#concat all elements of data_list
data = pd.concat(data_list)

#write concatenated data in to the final csv file
output_file_final = 'output_all.csv'
data.to_csv(output_file_final)
print("Final output written in to  : %s",output_file_final)
