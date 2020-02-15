"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

X = 10
Y = 2.24552
Z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of X,
# Y, and Z:
# X is 10, Y is 2.25, Z is "I like turtles!"
print("X is %s, Y is %s, Z is %s" % (X, Y, Z))

# Use the 'format' string method to print the same thing
print("X is {}, Y is {}, Z is {}".format(X, Y, Z))

# Finally, print the same thing using an f-string
print(f'X is {X}, Y is {Y}, Z is {Z}')
