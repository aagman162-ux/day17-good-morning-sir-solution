# Read the computer’s local hour and print a greeting for the matching time period.
import time

Mytime = time.strftime("%H:%M:%S")
# Convert the local hour to an integer so it can be compared with time ranges.
Hour =int( time.strftime("%H"))
# print(Hour)

if Hour>=0 and Hour<12:
    print("Good Morning Sir")
elif Hour>=12 and Hour<16:
    print("Good Afternoon Sir")
elif Hour>=16 and Hour<21:
    print("Good Evening Sir")
elif Hour>=21 and Hour<24:
    print("Good Night Sir")