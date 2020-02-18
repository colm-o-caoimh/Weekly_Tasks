# Weekly_Tasks

This repository contains my weekly homework for the Programming and Scripting module. I give an account of the process I went through in solving the problem and writing the code. 

(Week 1 Task: Set up Github account. Created first repository)

Week 2 Task: 
* Write program which calculates BMI. User inputs height and weight, program outputs BMI given these values. 
* My code varies slightly from the example given in Ian McLoughlin’s tutorial: I convert user input from string to int on the second line of code using the int() function. Ian’s code converted user input to float upon input entry.
* I used the round() function to round to two decimal places. I got this idea from a classmate’s suggestion on moodle discussion forum.

Week 3 Task:
* User inputs a sentence/string. Program outputs every second letter in reverse order.
* I had difficulty slicing the string correctly. Using the ‘start, stop, step’ logic to slicing using the indexing syntax (square brackets) learned on Codecademy, my code was as follows: reverse = phrase[-1:0:-2]. This will always exclude the element at index 0.
* Following some troubleshooting online (stackoverflow.com) I discovered that phrase[::-2] solved my issue

Week 4 Task:
* User inputs any positive integer. If input is even, divide by 2. If odd, multiply by 3 and add 1.
* As per the demonstration in the tutorial, I created a while loop which breaks once the current value is 1. 
* I also initialized an empty list to which each output calculated by the program is added.

Week 5 Task:
* Write a program which outputs whether today is a weekday or the weekend.
* My first instinct was to create a list/dictionary containing the days of the week, loop through that list, and break when the if condition was satisfied. I eventually managed to get this to work following initial difficulties (I was comparing each dictionary element with the today variable which prevented distinction between weekdays and weekend)
* As a result of the difficulty I had with the for loop, I managed to simplify the code to its current version – a simple if..else statement. 
* I needed to work out how to check if an int variable was between two int values. For this I used stackoverlow (https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers)


