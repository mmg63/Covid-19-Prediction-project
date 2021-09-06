'''
This code is implemented by Mustafa Mohammadi, graduate student of Mater degree from University of Tehran.

This code is for Covid-19 classification
There has been a dataset from the kaggle website

'''

import numpy as np
import matplotlib.pyplot as pl
import torch.nn as nn
import torchvision
import torch
import csv

# filepath = 'Covid-19_dataset/countermeasures_db_johnshopkins_2020_03_30.csv'
filepath = 'Covid-19_dataset/countermeasures_db_johnshopkins_2020_03_30.csv'
# get data from csv and transmitted it into torch array
data_array_of_lists = np.empty((10000, 29), dtype=object)
with open(filepath, mode='r') as csv_file:
    csv_dictionary = csv.DictReader(csv_file)
    print('fields\' name:')
    print(csv_dictionary.fieldnames)
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(f'Column names are {", ".join(row)}')
        data_array_of_lists[line_count] = row
        print(len(data_array_of_lists))
        line_count += 1
    else:
        # Processed data from csv file and fit to an np array
        csv_data = data_array_of_lists[0:line_count]
        csv_headers = csv_dictionary.fieldnames

        print(csv_data.shape)
        del data_array_of_lists, row, line_count



