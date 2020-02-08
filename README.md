# Weekly_Tasks
Weekly homework for Programming and Scripting module

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

