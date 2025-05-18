#This is a random integer exercise. Originally got it wrong, but after a hint was able to make it work as intended.

# NO TOUCHING ======================================
from random import randint
x = randint(-100, 100)
while x == 0:  # make sure x isn't zero
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:  # make sure y isn't zero
    y = randint(-100, 100)
# NO TOUCHING ======================================
 
# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# if x and y >= 0:     (this does not work) 
if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")