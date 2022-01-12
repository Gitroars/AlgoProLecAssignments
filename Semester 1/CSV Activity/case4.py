'''
1. Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating
whether a given date is a weekday or weekend

2. Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of
steps taken, averaged across all weekdays or weekends (y-axis).

'''
# Module Imports

import statistics as st
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('activity.csv') #read csv file
df.dropna(subset=["steps"],inplace=True) #remove rows that contains NaN
listDate = df["date"].to_list() #Make a list for dates
listWeektype = [] #Initialize a list for week types

for x in listDate:
    temp = pd.Timestamp(x) #Used for weekday function
    #Determine whether a date is weekday or weekend
    if temp.weekday() < 5 :
        listWeektype.append("Weekday")

    elif temp.weekday() >=5  :
        listWeektype.append("Weekend")

df['weektype'] = listWeektype #Create a new column for the week type based on the list


#Intialize dictionaries for interval of weekday and weekend
dictIntervalWeekday = {}
dictIntervalWeekend = {}

for i,row in df.iterrows(): #For each row,
    steps = row[0] #get the steps value
    interval = int(row[2]) #get the interval value
    type = row[3] #get the weektype value
    # check if row's weektype is weekday/weekend
    if type == "Weekday":
        dictIntervalWeekday.setdefault(interval, [])
        dictIntervalWeekday[interval].append(int(steps)) # adds steps per interval to weekday dictionary
    elif type == "Weekend":
        dictIntervalWeekend.setdefault(interval, [])
        dictIntervalWeekend[interval].append(int(steps)) # adds steps per interval to weekend dictionary


#Initialize list for average interval of weekday and weekend
listAvePerIntervalWeekday = []
listAvePerIntervalWeekend = []

for i in dictIntervalWeekday.keys():
    #Add the average value based on loop index of weekday interval dictionary to weekday average interval list
    listAvePerIntervalWeekday.append(st.mean(dictIntervalWeekday.get(i)))
for i in dictIntervalWeekend.keys():
    # Add the average value based on loop index of weekend interval dictionary to weekend average interval list
    listAvePerIntervalWeekend.append(st.mean(dictIntervalWeekend.get(i)))



# Create a plot for weekdays based on weekday dictionary and list
plt.plot(list(dictIntervalWeekday.keys()),listAvePerIntervalWeekday,c='blue')
plt.title("Average Weekday Activity")
plt.xlabel("Time Interval")
plt.ylabel("Average number of steps taken")
plt.show()

# Create a plot for weekends based on weekdend dictionary and list

plt.plot(list(dictIntervalWeekend.keys()),listAvePerIntervalWeekend,c='red')
plt.title("Average Weekend Activity")
plt.xlabel("Time Interval")
plt.ylabel("Average number of steps taken")
plt.show() #will be displayed after previous plot is closed

