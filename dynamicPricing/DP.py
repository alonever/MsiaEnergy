import csv
import numpy as np

def read_data(filename):
    with open(filename, 'r') as raw:
        reader = csv.reader(raw)
        reader.next()
        data = np.zeros(24)
        try:
            for row in reader:
                data[int(row[0]) - 1] = float(row[1].replace(",", ""))/365
        except ValueError:
            print "Flat rate usage data error"
            exit()
        return data
    
data = read_data('DP_usage.csv')
  
# print data
# [ 10697.838      10124.3790137   9793.9         9549.41        9685.3030137
#   10127.9450137  10863.3330137  11829.8230137  12795.698      13399.59
#   13931.046      14193.108      14449.156      14680.5770137  14888.316
#   14915.2210137  14843.4590137  14213.986      13558.818      12997.334
#   13130.054      12676.16       11855.984      10917.364    ]


# define parameters
off_peak_hr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 22, 23])
peak_hr = np.array([10, 11, 12, 13, 14, 15, 16, 17])
profit_margin = 0.13
fixed_cost = 591606483 / 365
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
deliver_cost = 50 # per MWh
spot_price = 60000 # per MW
capacity = 13400 # MW

# find total peak usage within the selected hours
# input load profile and the definition of the hours. By default is the whole day
def find_usage(load_profile, hr=range(24)):
    usage = 0.00
    for i in hr:
        usage += load_profile[i]
    return usage

D_p = find_usage(data, peak_hr)
D_op = find_usage(data, off_peak_hr)
# print D_p, D_op
# 116114.869041 184002.933068
def find_max(load_profile):
    Dmax = -np.inf
    for i in range(len(data)):
        if data[i] > Dmax:
            Dmax = data[i]
        else:
            pass
    return Dmax
Dmax=find_max(data)
spot_cost = (Dmax - capacity)*spot_price/365
# print spot_cost
# 249077.426909
def find_rev(load_profile):
    rev = find_usage(load_profile) * flat_rate
    return rev
# print find_rev(data)
# 27010602.1899
def find_exp(load_profile):
    exp = np.zeros(24)
    for i in range(len(data)):
        if data[i] < capacity:
            exp[i] = data[i] * deliver_cost
        else:
            exp[i] = capacity * deliver_cost
    totexp = sum(exp) + spot_cost + fixed_cost
    return totexp
# print find_exp(data)
# 16422122.1803
# print find_rev(data)-find_exp(data)
# 10588480.0095
# print (find_rev(data)-find_exp(data))/find_rev(data)
# 0.392011993479
