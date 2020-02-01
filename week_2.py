# Ask user to enter weight and height
# input value stored in variables user_weight and user_height
user_weight = input('Please enter your weight in kg: ')
user_height = input('Please enter your height in cm: ')

# Calculate BMI by dividing user weight by user height in metres squared
BMI = int(user_weight) / (int(user_height) / 100) ** 2

# Print BMI, rounding to 2 decimal places
print('Your BMI is: ' + str(round(BMI, 2)))