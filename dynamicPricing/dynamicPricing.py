# import pandas as pd
# 
# data = pd.read_csv('D:/MSIA/Courses/Spring13/MSIA 490/Week 5/DP_usage.csv', index_col = 'Hour')

import csv
import numpy as np



# read flat rate load profile data
def read_data(filename):
    with open(filename, 'r') as raw:
        reader = csv.reader(raw)
        header = reader.next()
        data = []
        for row in reader:
            data.append(row)
#         print header + data
        for i in range(len(data)):
            data[i][1] = float(str(data[i][1]).replace(",",""))
        return data

# find the maximum load under the flat rate profile    
def find_max():
    Dmax = -np.inf
    for i in range(len(data)):
        if data[i][1] > Dmax:
            Dmax = data[i][1]
        else:
            pass
        return Dmax

# find total peak usage under flat rate
def find_D_p():
    peak_hr = [0,1,2,3,4,5,6,7,8,9,18,19,20,21,22,23]
    usage_peak = 0.00
    for i in peak_hr:
        usage_peak += data[i][1]
    return usage_peak

# find total off-peak usage under flat rate    
def find_D_op():
    off_peak_hr = [10,11,12,13,14,15,16,17]
    usage_off_peak = 0.00
    for i in off_peak_hr:
        usage_off_peak += data[i][1]
    return usage_off_peak

# find off-peak price if given peak price
def off_peak_price():
    pass

# find peak price if given off-peak price
def peak_price():
    pass

# Execute
data = read_data('D:/MSIA/Courses/Spring13/MSIA 490/Week 5/DP_usage.csv')

# set parameters
x_p = 0                             # peak rate
x_op = 1                            # off-peak rate
v = x_p/x_op                        # peak/off-peak price ratio
q = np.power(v, -0.016033333)
D_p = find_D_p()                    # peak usage under flat rate
D_op = find_D_op()                  # off-peak usage under flat rate
D_max = find_max()                  # maximum usage under flat rate
print D_p
print D_op
print D_max 