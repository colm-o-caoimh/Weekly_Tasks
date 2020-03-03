# Colm O'Caoimh
# Write a program that reads in a text file
# and outputs the number of e's it contains. 
# The program should take the filename from 
# an argument on the command line.

#(first attempt)
 
# Prompt user to input filename on command line
filename = input('Enter filename, path or directory you wish to submit: ')

# Use with statement to open and close file
with open(filename, 'r') as f:
    x = f.read()
    # Use count method to output number of e's
    print(x.count('e'))
