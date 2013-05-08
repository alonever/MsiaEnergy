import csv
import numpy as np

def read_data(filename):
    with open(filename, 'r') as raw:
        reader = csv.reader(raw)
        reader.next()
        data = np.zeros(24)
        try:
            for row in reader:
                data[int(row[0]) - 1] = float(row[1].replace(",", ""))
        except ValueError:
            print "Flat rate usage data error"
            exit()
        return data
    
data = read_data('DP_usage.csv')

# print data
# [ 3904710.87  3695398.34  3574773.5   3485534.65  3535135.6   3696699.93
#   3965116.55  4317885.4   4670429.77  4890850.35  5084831.79  5180484.42
#   5273941.94  5358410.61  5434235.34  5444055.67  5417862.54  5188104.89
#   4948968.57  4744026.91  4792469.71  4626798.4   4327434.16  3984837.86]

# define parameters
off_peak_hr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 22, 23])
peak_hr = np.array([10, 11, 12, 13, 14, 15, 16, 17])
profit_margin = 0.13
fixed_cost = 591606483
# the daily usage elasticity
def q(v):
    return np.power(v, -0.016033333)
# the peak usage/off-peak usage changes
def g(v):
    return np.power(v, -0.2133333)
# reduction in peak load consumption as a percentage of the maximum load under the flat rate profile
def l(v):
    return np.power(v - 1, 0.441066) / 100
flat_rate = 0.09 * 1000  # per MWh
deliver_cost = 50
spot_price = 60000
capacity = 13400 * 365

