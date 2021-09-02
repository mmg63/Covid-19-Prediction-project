'''
This code is implemented by Mustafa Mohammadi, graduate student of Mater degree from University of Tehran.

This code is for Covid-19 classification
There has been a dataset from the kaggle website

'''

import numpy as np
import matplotlib.pyplot as pl
import torch.nn as nn
import torchvision
import csv

# filepath = 'Covid-19_dataset/countermeasures_db_johnshopkins_2020_03_30.csv'
filepath = 'Covid-19_dataset/COVID 19 Containment measures data.csv'
with open(filepath, mode='r') as csv_file:
    csv_dictionary = csv.DictReader(csv_file)
    print('fields\' name:')
    print(csv_dictionary.fieldnames)
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

