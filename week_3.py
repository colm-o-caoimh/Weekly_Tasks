# Colm O Caoimh
# Write a program that asks a user to input a string and outputs every second letter in reverse order. 

# Ask user to enter a sentence
phrase = input("Please enter a sentence: ")

# Use string slicing to select every second character in reverse order. Store the result in variable 'reverse'
reverse = phrase[::-2]

# print result 
print(reverse)

# References
# stackoverflow.com https://stackoverflow.com/questions/43905517/how-to-do-reverse-slicing-in-python
# VanderPlas, Jake; A Whirlwind Tour of Python (Chapter 1); https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
