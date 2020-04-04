# Colm O Caoimh
# Write a program that calculates the user's Body Mass Index (BMI).

# user input value stored in variables user_weight and user_height
user_weight = input('Please enter your weight in kg: ')
user_height = input('Please enter your height in cm: ')

# Calculate BMI by dividing user weight by user height in metres squared
BMI = int(user_weight) / (int(user_height) / 100) ** 2

# Print BMI, rounding to 2 decimal places
print('Your BMI is: ' + str(round(BMI, 2)))

# References
# Moodle module class forum: https://learnonline.gmit.ie/mod/forum/discuss.php?d=6133

