# Weekly_Tasks

**This repository contains my weekly homework for the Programming and Scripting module. I give an account of the process I went through each week in solving the problem and writing the code.** 

(Week 1 Task: Set up Github account. Created first repository)

### Week 2 Task: 
* Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared. 
* My code varies slightly from the example given in Ian McLoughlin’s tutorial: I convert user input from string to int on the second line of code using the `int()` function. Ian’s code converted user input to float upon input entry.
* I used the `round()` function to round to two decimal places. I got this idea from a classmate’s suggestion on moodle discussion forum.

### Week 3 Task:
* Write a program that takes asks a user to input a string and outputs every second letter in reverse order. 
* I had difficulty slicing the string correctly. Using the ‘start, stop, step’ logic to slicing using the indexing syntax (square brackets) learned on Codecademy, my code was as follows: `reverse = phrase[-1:0:-2]`. This will always exclude the element at index 0.
* Following some troubleshooting online (stackoverflow.com) I discovered that `phrase[::-2]` solved my issue

### Week 4 Task:
* Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
* As per the demonstration in the tutorial, I created a while loop which breaks once the current value is 1. 
* I also initialized an empty list to which each output calculated by the program is added.

### Week 5 Task:
* Write a program that outputs whether or not today is a weekday.
* My first instinct was to create a list/dictionary containing the days of the week, loop through that list, and break when the if condition was satisfied. I eventually managed to get this to work following initial difficulties (I was comparing each dictionary element with the today variable which prevented distinction between weekdays and weekend)
* As a result of the difficulty I had with the for loop, I managed to simplify the code to its current version – a simple if..else statement. 
* I needed to work out how to check if an int variable was between two int values. For this I used stackoverlow (https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers)

### Week 6 Task:
* Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 
* Having familiarised myself with function syntax learned in the video lectures, I went about attempting to work out a mathematical formula to solve the problem. I tried to establish a mathematical connection between the numbers whose square roots are natural numbers (1, 4, 9, 16, 25, 36 etc.) I tried various other simple calculations (N/2, N/2 - ?N etc.) to see if I could establish connections to include in a formula. This yielded some interesting results but was not helpful for the task at hand.
* I came to realise that multiplying a number by itself might be the key to coming up with the formula. I managed to write a function which returned the square route of a natural number, by using the `range()` function and iterating over each number until one of the numbers squared equalled the number input by the user. The range function however did not allow me to iterate over floating point numbers.
* I eventually managed to produce the desired result by creating a while loop, initialising a count variable to zero, and adding 0.01 on each iteration. The number being iterated over was squared on each iteration until it matched the number input by the user. 
* My formula suffers from inefficiency, particularly if the number entered by the user is very big. It is also a rather crude approximation of the square root, but this is what was task asked for so it met the goal at least.
* When multiplied and added, floating point numbers do not behave as I expected, with many numbers after the decimal points causing difficulty for my formula. I had to compensate by using the `round()` function a lot to get the desired result. This was very time consuming but very informative. I learned a lot doing this.
* I found Newton’s method online after completing the program. While the mathematical formula itself is quite easy to understand, the coded function contains a concept which I would like to give more time to understanding (‘precision’ variable). 
* I benefitted a lot from this week’s exercise, particularly as I managed to overcome the challenge which had stumped me for quite a while. The perseverance paid off. It also gave me an insight into the difficulty around writing an efficient function for a seemingly simple problem. Coupled with the information in the lectures, I have begun to realise how this can be a massive area of importance in the world of programming. It also solidified my understanding of the difference between a function and an algorithm, which was nicely explained by Ian in the videos. 

### Week 7 task:
* Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.
* I was unsure of the precise meaning of the task instruction. I did not realise that arguments could be taken from the command line. I posted a question to the class forum on Moodle and discussed it with classmates.
* My initial attempt involved a prompt for the user to input file name on the command line but this was not exactly what was demanded by the task.
* Following a little more research I discovered that through the sys module, arguments from the command line could be passed through the program using the `sys.argv` list. I used stackoverflow for this (https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162).
* This produced the desired result for this week’s task
	
### Week 8 task:
* Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
* This week’s task was relatively straight forward for me as it mirrored the video lecture almost exactly. In addition, I have been following courses on Datacamp which have served as an introduction to Numpy and Matplotlib. 
* I tinkered a bit with the third parameter in the `np.arange()` function in order to get a curved line in the plot. This was purely for aesthetic purposes as it is more appealing to the eye. 
* This exercise allowed me to become more familiar with using ipython on the command line. I can see how convenient it might be for this type of work. The %logstart command is something I made use of here and will be using in future for similar projects.



