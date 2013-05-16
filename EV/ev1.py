
from psycopg2 import connect
import pandas as pd
import numpy as np
import pandas.io.sql as psql
import matplotlib.pyplot as plt
from collections import Counter

###################
# # connect to db ##
###################
con = connect(user="postgres", host="localhost", database="EV")

# select all columns from database as lists
frame = pd.DataFrame(
    {'idnum': np.array(psql.tquery('select id from ev_charging;', con=con)),
    'startday' : np.array(psql.tquery('select startday from ev_charging;', con=con)),
    'starttime' : np.array(psql.tquery('select starttime from ev_charging;', con=con)),
    'timezone' : np.array(psql.tquery('select timezone from ev_charging;', con=con)),
    'duration' : np.array(psql.tquery('select duration from ev_charging;', con=con)),
    'energy' : np.array(psql.tquery('select energy from ev_charging;', con=con)),
    'ghgsavings' : np.array(psql.tquery('select ghgsavings from ev_charging;', con=con)),
    'englevel' : np.array(psql.tquery('select englevel from ev_charging;', con=con)),
    'address' : np.array(psql.tquery('select address from ev_charging;', con=con))
})
# print data

# clean address, then specify city, state, zip code
city = []
statezip = []
state = []
zipcode = []
for i in range(len(frame['address'])):
    string = frame['address'][i].split(', ')
    if string[2] != 'Bourbonnais':
        city.append(string[1])
        statezip.append(string[2])
    else:
        city.append(string[2])
        statezip.append(string[3])
for i in range(0, len(statezip)):
    string = statezip[i].split(' ')
    state.append(string[0])
    zipcode.append(string[1])

ct_state = Counter(state)
state_name = []
state_num = []
for key in ct_state:
    state_name.append(key)
    state_num.append(int(ct_state[key]))
city_name = []
city_num = []
ct_city = Counter(city)
for key in ct_city:
    city_name.append(key)
    city_num.append(int(ct_city[key]))
    
# count englevels - TRIVIAL b/c all level 2
# ct_englevel = psql.tquery('select englevel, count(*) from ev_charging group by englevel;', con=con)
# count timezones
# ct_timezone = psql.tquery('select timezone, count(*) from ev_charging group by timezone;', con=con)

# calculating total energy by date
energy_by_day = psql.tquery('select startday, sum(energy) from ev_charging group by startday;', con=con)
date = [x for (x, y) in energy_by_day]
epd = [y for (x, y) in energy_by_day]

# calculate charging durations in minutes by date
# duration_by_day = psql.tquery('select startday, extract(minutes from sum(duration::interval))+extract(hours from sum(duration::interval))*60 as "Duration" FROM ev_charging group by startday;', con=con)
# date = [x for (x,y) in duration_by_day]
# duration = [y for (x,y) in duration_by_day]

####################
# # start plotting ##
####################
width = 0.35
ind = np.arange(len(state_name))
plt.figure(1)  # the first figure
plt.bar(ind, state_num, width=width, align='center', color='red')
plt.xticks(ind, state_name)
plt.title("Number of Chargings by State")

plt.figure(2)  # a second figure
plt.scatter(date, epd)
plt.xticks(rotation=25)
plt.title("Energy Consumed per Day")
plt.ylim(-10, 350)
plt.show()
