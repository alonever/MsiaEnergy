# import pandas as pd
# 
# data = pd.read_csv('D:/MSIA/Courses/Spring13/MSIA 490/Week 5/DP_usage.csv', index_col = 'Hour')

import csv
import numpy as np

def read_data():
    with open('D:/MSIA/Courses/Spring13/MSIA 490/Week 5/DP_usage.csv', 'r') as raw:
        reader = csv.reader(raw)
        header = reader.next()
        data = []
        for row in reader:
            data.append(row)
        print header + data
    
