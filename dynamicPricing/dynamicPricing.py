import csv
import numpy as np

# read flat rate load profile data
# output is a float array with 24 elements, the index is (the corresponding hour-1)
def read_data(filename):
    with open(filename, 'r') as raw:
        reader = csv.reader(raw)
        header = reader.next()
        data = np.zeros(24)
        try:
            for row in reader:
                data[int(row[0]) - 1] = float(row[1].replace(",", ""))
        except ValueError:
            # Conversion failed
            print "Flat rate usage data error"
            exit()
#        print data
        return data

# find the maximum load under the flat rate load profile    
# input load profile
# return the hour with maximum load
def find_max(load_profile):
        return np.where(load_profile == max(load_profile))[0][0] + 1

# find total peak usage within the selected hours
# input load profile and the definition of the hours. By default is the whold day
def find_usage(load_profile,peak_hr=range(24)):
    usage = 0.00
    for i in peak_hr:
        usage += data[i]
    return usage

# find off-peak price if given peak price
def off_peak_price():
    pass

# find peak price if given off-peak price
def peak_price():
    pass

# Execute
data = read_data('DP_usage.csv')
print find_max(data)
off_peak_hr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 22, 23])
peak_hr = [10, 11, 12, 13, 14, 15, 16, 17]
print find_usage(data)
print find_usage(data,peak_hr)
print find_usage(data,off_peak_hr)

