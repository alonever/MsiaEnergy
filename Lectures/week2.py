# NumPy
import numpy as np

a = range(3,5,0.1) # does not work!
a = np.array([1,3,4,6])
a = np.arange(3,5,0.1) # this one works!
a = [1,2,'adfsada',3.5]
a = np.array([1,2,'asdfa',3.5]) # all inputs are strings now!
a = [[1,2], [3,4]]
a = np.zeros((3,2), dtype=np.float)
a = np.identity(3)
b = a + 1
c = 2 * b
c * c
d = np.dot(c, c)
c = np.array([[1,2,0], [5,4,5], [2,6,8]])
np.invert(c)

import numpy.linalg as la
dir(la)

# PANDAS
from pandas import *
dates = np.asarray(date_range("1/1/2013", periods = 12))
df = DataFrame(randn(12,4), index=dates, columns = ['A', 'B', 'C', 'D'])