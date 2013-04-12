from datetime import datetime as datetime

x = datetime.now()
print x

s = "I'm" + ' so f"k" hungry!'
print s

b = 2/3
print b

b = 2.0/3
print b

x = ["hi", 2.0, -5] # list
print x[0]
print x[2]
print x[1]
x[0]="MSIA" # change list value
print x

t = ("pi", "e") # tuple
print t

d = {"PI": 3.14159265, "e": 2.71828} # dictionary
print d["PI"]
d["CN"] = "ce na" # insert new key and value
print d

newx = x # duplicate list
newx[0] = "hi again" # change both lists
print x

# in class exercise
a = dict(zip(range(10), [x*x for x in range(10)]))
print a
a[5] = 30
a["nu"] = 100
print a
del a[0]
print a

import math
i=0.5
calc = i+1
print calc