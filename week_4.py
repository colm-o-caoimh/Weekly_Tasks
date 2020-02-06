# Colm O'Caoimh
# If input is even, divide by 2. If odd, multiply by 3 and add 1

# Ask user to input any positive integer
x = int(input("Enter any positive integer: "))

y =[]

# Create while loop which breaks once the current value is 1 
while x > 1:
    if x % 2 == 0:
        x = x / 2
        # print(x)
    else:
        x % 2 != 0
        x = (x * 3) + 1
        # print(x)
    print(x)
    y.append(int(x))

print(y)