from datetime import datetime
import calender

# to print date and time
 print(datetime.now())
  
 #to print the calender
print(calendar.month(2019,8)) # you can change the year and month attributes

b = str(datetime.now()) # convering the date time to string

c = b.split() # spliting the string to blocks

year_array = c[0].split("-") # spliting the string to blocks like year month date and time

year = int(year_array[0]) # 0th index has year so accesing it  you can even print to ensure

month = int(year_array[1]) # 1th index has month 

