# https://www.geeksforgeeks.org/python-datetime-strptime-function/#:~:text=strptime%20%28%29%20is%20another%20method%20available%20in%20DateTime,format%20to%20date-time%20object.%20Syntax%3A%20datetime.strptime%20%28time_data%2C%20format_data%29?msclkid=b313a73bc5f811eca99f06366f0fc5bd
import datetime
import _strptime
fecha = '2022-01-20'

# import datetime module from datetime
from datetime import datetime
 
# consider the time stamp in string format
# DD/MM/YY H:M:S.micros
time_data = "25/05/99 02:35:5.523"
 
# format the string in the given format :
# day/month/year hours/minutes/seconds-micro
# seconds
format_data = "%d/%m/%y %H:%M:%S.%f"
 
# Using strptime with datetime we will format
# string into datetime
date = datetime.strptime(time_data, format_data)

# display milli second
print(date.microsecond)
 
# display hour
print(date.hour)
 
# display minute
print(date.minute)
 
# display second
print(date.second)
 
# display date
print(date)