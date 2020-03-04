# Colm O'Caoimh
# Write a program that reads in a text file
# and outputs the number of e's it contains. 
# The program should take the filename from 
# an argument on the command line.


# Import sys module to enable program to take file name/path
# from argument on command line
import sys

# Use with statement to open and close file
# Count e's using count method
with open(sys.argv[1], 'r') as f:
    readfile = f.read()
    print(readfile.count('e'))
