"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use
parens instead of square brackets.

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values
never needs to be mutated, use a tuple instead of a list.

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically.
"""

# Example:

import math

def dist(_a, _b):
    """Compute the distance between two x,y points."""
    _x0, _y0 = _a  # Destructuring assignment
    _x1, _y1 = _b

    return math.sqrt((_x1 - _x0)**2 + (_y1 - _y0)**2)

A = (2, 7)   # <-- x,y coordinates stored in tuples
B = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(A, B)))



# Write a function `print_tuple` that prints all the values in a tuple

# YOUR CODE HERE
def print_tuple(some_tuple):
    """Print all value in the passed in tuple"""
    for i in some_tuple:
        print(i)

T = (1, 2, 5, 7, 99)
print_tuple(T)  # Prints 1 2 5 7 99, one per line

# Declare a tuple of 1 element then print it
U = (1,)  # What needs to be added to make this work? A trailing comma.
print_tuple(U)
