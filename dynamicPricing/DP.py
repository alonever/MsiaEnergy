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

