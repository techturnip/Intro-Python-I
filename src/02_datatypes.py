"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

X = 5
Y = "7"

# Write a print statement that combines X + Y into the integer value 12

# YOUR CODE HERE
print(X + int(Y))

# Write a print statement that combines X + Y into the string value 57

# YOUR CODE HERE
print(str(X) + Y)
