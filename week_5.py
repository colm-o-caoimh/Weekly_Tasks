# Colm O'Caoimh
# Write a program which outputs whether today is a weekday or not

# import datetime module.
import datetime
 
# Create variable 'now' to store current time and date.
now = datetime.datetime.now()

# Create variable 'today' to store current weekday.
today = now.weekday()

# Create dictionary assigning .weekday() method int to corresponding day in English.
days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

# Write if-else statement to separate weekdays from weekend 
if 0 <= today <= 4:
    print("Today is " + days[today] + ", a weekday unfortunately. Back to work!")
else:
    print("It's " + days[today] + ", it's the weekend. Hooray!!")

# References
# stackoverflow.com: https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers
# VanderPlas, Jake; A Whirlwind Tour of Python (Chapter 1), https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf

