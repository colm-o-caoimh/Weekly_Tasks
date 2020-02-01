# Ask user to enter a sentence
phrase = input("Please enter a sentence: ")

# Use string slicing to select every second character in
# reverse order. Store the result in variable 'reverse'
reverse = phrase[::-2]

# print result 
print(reverse)