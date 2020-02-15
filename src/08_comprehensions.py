"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

Y = [x+1 for x in range(5)]

print(Y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

Y = [x**3 for x in range(10)]

print(Y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

A = ["foo", "bar", "baz"]

Y = [ele.upper() for ele in A]

print(Y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

X = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?

# creates list of nums regardless of format ie. '1,2,3,4...' or '1, 2, 3, 4...'
Y = [int(num) for num in X if int(num) % 2 == 0]

print(Y)
