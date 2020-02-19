"""
Use methods and functions that are available for Python Lists
"""
# For the exercise, look up the methods and functions that are available for use
# with Python lists.

X = [1, 2, 3]
Y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change X so that it is [1, 2, 3, 4]
# YOUR CODE HERE
X.append(4)
print(X)

# Using Y, change X so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
for v in Y:
    X.append(v)
print(X)

# Change X so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
# for v in X:
#     if v == 8:
#         X.remove(v)
X.remove(8)
print(X)

# Change X so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
for (i, v) in enumerate(X):
    if v == 9:
        X.insert(i + 1, 99)
print(X)

# Print the length of list X
# YOUR CODE HERE
print(len(X))

# Print all the values in X multiplied bY 1000
# YOUR CODE HERE
for v in X:
    print(v * 1000)
