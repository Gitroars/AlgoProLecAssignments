def convertToDays():
  #User input 3 time values
    hours = int(input("Enter number of hours:"))
    minutes = int(input("Enter number of minutes:"))
    seconds = int(input("Enter number of seconds:"))

    def getDays(h,m,s):
      #Calculate days by dividing amount of time unit available in a day then add it and round the value to 4 decimals
        days = round((h / 24 + m / 1440 + s / 86400),4)
        return days
    #Calls the helper function with inputted value
    newDays = getDays(hours,minutes,seconds)
    print("Total of days is: ",newDays)
#Calls the function
convertToDays()

