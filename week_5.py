# Colm O'Caoimh
# Write a program which outputs whether today is a weekday or not

import datetime

#days = [0, 1, 2, 3, 4, 5, 6] 


now = datetime.datetime.now()
today = now.weekday()
if 0 >= today >= 4:
    print('Unfortunately today is a weekday. Back to work!')
else:
    print("It's the weekend. Hooray!!")

print(now.time())
    