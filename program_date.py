# import date
from datetime import date

# print today's date with the prefix "Today is "
# use the date.today() function

print("Today is ",date.today()) 

print("Today's date is: " + str(date.today()))   

# unit conversion

parsec = 3.26 # lightyears
parsecs = 11
lightyears = parsecs * parsec

print("11 parsecs is equal to ",lightyears," lightyears")
