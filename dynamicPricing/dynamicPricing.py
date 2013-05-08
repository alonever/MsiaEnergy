import csv
import numpy as np

# read flat rate load profile data
# output is a float array with 24 elements, the index is (the corresponding hour-1)
def read_data(filename):
    with open(filename, 'r') as raw:
        reader = csv.reader(raw)
        reader.next()
        data = np.zeros(24)
        try:
            for row in reader:
                data[int(row[0]) - 1] = float(row[1].replace(",", ""))
        except ValueError:
            # Conversion failed
            print "Flat rate usage data error"
            exit()
        return data

# find total peak usage within the selected hours
# input load profile and the definition of the hours. By default is the whole day
def find_usage(load_profile, hr=range(24)):
    usage = 0.00
    for i in hr:
        usage += load_profile[i]
    return usage

# assume bill neutrality
# find off-peak price given original load profile, peak price, peak and off_peak_hr, and flat price (per MWh)
def off_peak_price(x_p, load_profile, peak_hr, off_peak_hr, flat_rate):
    u_p = find_usage(load_profile, peak_hr)
    u_op = find_usage(load_profile, off_peak_hr)
    x_op = (flat_rate * (u_p + u_op) - x_p * u_p) / u_op
    return x_op

# find off-peak price given original load profile, peak price, peak and off_peak_hr, and flat price (per MWh)def peak_price(data, x_p, peak_hr, off_peak_hr, flat_rate):
def peak_price(x_op, load_profile, peak_hr, off_peak_hr, flat_rate):
    u_p = find_usage(load_profile, peak_hr)
    u_op = find_usage(load_profile, off_peak_hr)
    x_p = (flat_rate * (u_p + u_op) - x_op * u_op) / u_p
    return x_p

# find the new load profile under the peak and off-peak price
def newLoad(load_profile, peak_hr, off_peak_hr, v):
    new_load_profile = np.empty_like(load_profile)
    # total peak usage under the flat rate
    D_p = find_usage(data, peak_hr)
    # total off-peak usage under the flat rate
    D_op = find_usage(data, off_peak_hr)
    # total peak usage under the TOU rate
    U_p = (D_p + D_op) * q(v) / (1 + D_op / D_p / g(v))
    # total off-peak usage under the TOU rate
    U_op = (D_p + D_op) * q(v) / (1 + D_p * g(v) / D_op)
    new_load_profile[peak_hr] = U_p / set(peak_hr).__len__()
    new_load_profile[off_peak_hr] = U_op / set(off_peak_hr).__len__()
    return new_load_profile

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
# unit costs per MWh
flat_rate = 0.09 * 1000  # per MWh
deliver_cost = 50
spot_price = 60000
capacity = 13400 * 365

# Unit testing read_data function
data = read_data('DP_usage.csv')
# Unit testing off_peak_price, and find_usage function,
# by setting peakprice=150 dollar per MWh
print "Suppose peak price is 150 dollar per MWh"
x_p = 120
x_op = off_peak_price(x_p, data, peak_hr, off_peak_hr, flat_rate)
v = x_p / x_op
print "x_op=" + str(x_op)
print "v=" + str(v)
print "new load profile"
new_load_profile = newLoad(data, peak_hr, off_peak_hr, v)
for i in range(24):
    print "hour #" + str(i + 1) + ":" + str(new_load_profile[i])
print capacity
