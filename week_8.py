 # Colm O'Caoimh
 
 # Write a program that displays a plot of the functions 
 # f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. 

# Import relevant modules, numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Create a numpy array in the range [0, 4] and set to variable x.
# The third parameter (0.1) is added for nicer data visualisation 
# as it smooths the plot lines.
x = np.arange(0.0, 4.0, 0.1)

# Create variables for the functions as per Week 8 task
f = x
g = x**2
h = x**3

# Plot each function in the range specified
plt.plot(x, f)
plt.plot(x, g)
plt.plot(x, h)

# Show plot
plt.show()

# References
# https://www.datacamp.com/
