# Colm O'Caoimh
# Define a function which calculates the approximate square route of
# a positive floating point number


# User inputs positive floating point number
x = float(input('Please enter a positive number: '))

# Write function to calculate approximate square route
def sqrt(x):
    # Initialize variable count to 0. 
    count = 0
    # While loop iterates through count values,
    # incrementing by 0.01 each iteration
    while x > count:
        # Round count down to 2 decimal places as this is an approximation.
        # Set to variable a
        a = round(count, 2)
        # Set variable b to count ** 2 
        b = round(a ** 2, 1)
        # If statement breaks when count ** 2 = user input
        if b == round(x, 1):
            print('The square root of', x, 'is approx.', round(a, 1))
            break 
        # Gradually increment until square root is established
        count += 0.01

# Function call
sqrt(x)

