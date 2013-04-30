import pandas as pd

data = pd.read_csv('D:/MSIA/Courses/Spring13/MSIA 490/Week 5/DP_usage.csv', index_col = 'Hour')

print data[:24]