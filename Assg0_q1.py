import math
from sys import exit

print "Hello customer, welcome to the Bank of Python. How may I help you? (1 for investment; 2 for exit)"
option = int(raw_input("> "))
if option != 1:
    print "Thank you for banking with us! Goodbye!"
    exit()
print "Please enter the number of years you want to invest for"
t = int(raw_input("> "))
print "Please enter the initial value of your investment"
m = float(raw_input("> "))
print "Please enter the expected interest rate as a number of percentage (i%) of your investment"
i = float(raw_input("> "))

FV = math.pow((i/100+1), t) * m
print "The future value of your investment (NPV=$%d) after %d years will be $%d, if your expected interest rate of %d%% is possible" % (m, t, FV, i) 
print "You don't have enough money in your account for this investment."
print "Thank you for banking with us! Goodbye!"
exit()