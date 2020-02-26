# Weekly_Tasks

This repository contains my weekly homework for the Programming and Scripting module. I give an account of the process I went through each week in solving the problem and writing the code. 

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

Week 6 Task:
* Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 
* Having familiarised myself with function syntax learned in the video lectures, I went about attempting to work out a mathematical formula to solve the problem. I tried to establish a mathematical connection between the numbers whose square roots are natural numbers (1, 4, 9, 16, 25, 36 etc.) I tried various other simple calculations (N/2, N/2 - ?N etc.) to see if I could establish connections to include in a formula. This yielded some interesting results but was not helpful for the task at hand.
* I came to realise that multiplying a number by itself might be the key to coming up with the formula. I managed to write a function which returned the square route of a natural number, by using the range function and iterating over each number until one of the numbers squared equalled the number input by the user. The range function however did not allow me to iterate over floating point numbers.
* I eventually managed to produce the desired result by creating a while loop, initialising a count variable to zero, and adding 0.01 on each iteration. The number being iterated over was squared on each iteration until it matched the number input by the user. 
* My formula suffers from inefficiency, particularly if the number entered by the user is very big. It is also a rather crude approximation of the square root, but this is what was task asked for so it met the goal at least.
* When multiplied and added, floating point numbers do not behave as I expected, with many numbers after the decimal points causing difficulty for my formula. I had to compensate by using the round() function a lot to get the desired result. This was very time consuming but very informative. I learned a lot doing this.
* I found Newton’s method online after completing the program. While the mathematical formula itself is quite easy to understand, the coded function contains a concept which I would like to give more time to understanding (‘precision’ variable). 
* I benefitted a lot from this week’s exercise, particularly as I managed to overcome the challenge which had stumped me for quite a while. The perseverance paid off. It also gave me an insight into the difficulty around writing an efficient function for a seemingly simple problem. Coupled with the information in the lectures, I have begun to realise how this can be a massive area of importance in the world of programming. It also solidified my understanding of the difference between a function and an algorithm, which was nicely explained by Ian in the videos. 


