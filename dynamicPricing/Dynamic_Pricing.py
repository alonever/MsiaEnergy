#Energy - Dynamic Pricing

#Authored by:  Joseph Riley, Maria Virginia Rodriguez, Colin Watts-Fitzgerald

#loading libraries
import csv
import numpy as np
filename = "DP_usage.csv"

#other global variable definitions
dp = 0
dop = 0
peaklist = [] #peak usage list
offpeaklist = [] #off-peak usage list
flat_rate=90 #90 dollars per MWH

#######################################################
#
# Read Data
# The following function will read in a csv and parse into a dictionary.
# We will extract out hour and usage key-value pairs and calculate peak and off-peak usage
#
#######################################################
def readData(filename):
    
    global dp, dop
    
    #empty list creation
    rawdata = []
    usagelist = []

    reader = csv.DictReader(open(filename))
    
    #reading raw data - conversion to float on usage for calculations
    for row in reader:
        row['Usage (MWh)'] = float(row['Usage (MWh)'].replace(',',''))/365
        row['Hour'] = int(row['Hour'])
        rawdata.append(row)
        usagelist.append(row['Usage (MWh)'])
 
    #generate summed dp and dop values for peak and off-peak usage
    for i in range(len(rawdata)):
        hour = rawdata[i]['Hour']    
        if (hour >= 10 and hour <=17):
            peaklist.append(rawdata[i]['Usage (MWh)'])
            dp = dp + rawdata[i]['Usage (MWh)']
        else:
            offpeaklist.append(rawdata[i]['Usage (MWh)'])
            dop = dop + rawdata[i]['Usage (MWh)']
    dp=dp
    dop=dop
  
    
    return usagelist, peaklist, offpeaklist, dp, dop
#read data end

######################################
#
# Load Redistribution
# This function will redistribute the peak load reduction under the new curve
######################################

def load_redistribution(xp, xop):
    global peaklist 
    global offpeaklist
    global dp, dop, up, uop, New_peak_load, New_off_peak_load, New_load
    
    #redistribute loads for peak and offpeak times
    #Lv,Gv,Qv are our functions identifying load shifts, usage ratios, and elasticity
    
    Ratio = xp/xop
    Lv=1-((np.power((Ratio-1),0.441066))/100)
    Gv=np.power(Ratio,-0.2133333)
    Qv=np.power(Ratio,-0.016033333)
    New_peak_load = []
    New_off_peak_load = []
    #This loop calculates our percentage shift from our Dp to the new load during each hour and then calculates up
    for item in peaklist:
        New_peak_load.append(Lv*item)
    up = sum(New_peak_load)
    uop = ((dp+dop)*Qv)/(1+(dp/dop)*Gv) 
    
    #this loop uses our combined equations of Gv and Qv to find the shift as a ratio of our Dop to the new load during each hour
    for item in offpeaklist:
        New_off_peak_load.append((uop)*(item/dop))
        
    New_load=New_peak_load+New_off_peak_load    
    
    return New_peak_load, New_off_peak_load, up, uop,New_load
#load distribution end

#function calculating xp (peak price) from being given xop (off peak price) and bill neutrality


#####################################
#
# Finding Peak price when given off peak price using bill neutrality
#
#####################################
def peak_price(xop):
    global xp
    
    xp=((dp+dop)*flat_rate-dop*xop)/dp
    
    return xp


###### MAIN FUNCTION

###Run data read in function (gives us dp, dop, load lists
readData(filename)
xop=0
cost_output={}

#iterate over constrained range of xop
for xop in np.arange(0.01,89.99,0.01):
    cost1=0
    
#call peak price calculation function for each value of xop, we get an xp 
    peak_price(xop)

#call load redistribution function now that we have both xop and xp to caclulate up and uop as well as New_load list
    load_redistribution(xp,xop)

#maxused is our maximum load at a certain hour so we have a value to compare how much more capacity will need to be bought
    maxused=max(New_load)
    
#calculate objective function over all 24 hours (i) in our New load for both deliver costs and new capacity costs (daily cost)    
    for i in New_load:
        cost1=50*(min(i,13400))+(60000/365)*(maxused-13400)+cost1
        
#Profit restriction constraint outputs our objective value to a list with key of xop if the constraint is met
#outputs an "infinity" if the constraint is not met
# By using infinitys when we go to minimize, these values cannot be chosen        
    if 0.13>= ((xp*up+xop*uop)-cost1-(591606483/365))/(xp*up+xop*uop):
        cost_output[xop] = cost1
    else: 
        cost_output[xop] = float("inf")
#this profit calculation has been left in for diagnostic purposes, as it is/was useful to keep track of these values        
    profit=(xp*up+xop*uop)-cost1-(591606483/365)
#    print(profit)
         



#####################################
#
# Function Calls
#
#####################################

#print(sorted(cost_output.iteritems(), key=lambda(k,v): (v,k)))

#The following lines output our xop that gives us our minimum cost (which is also output) then calculates the corresponding xp
# There should be an output of a list of 2 values {xop, cost objective value} and a single value xp
minin = min(cost_output.values())
for k,v in sorted(cost_output.iteritems(), key=lambda(k,v): (v,k)):
    if v == minin:
        minxop = k,v
        print k,v
print(peak_price(minxop[0]))
