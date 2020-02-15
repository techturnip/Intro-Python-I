"""
Experiment with positional arguments, arbitrary arguments, and keyword
arguments.
"""

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def _f1(_n1, _n2):
    return _n1 + _n2

print(_f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def _f2(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(_f2(1))                    # Should print 1
print(_f2(1, 3))                 # Should print 4
print(_f2(1, 4, -12))            # Should print -7
print(_f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

A = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(_f2(*A))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def _f3(_n1, _n2=1):
    return _n1 + _n2

print(_f3(1, 2))  # Should print 3
print(_f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def _f4(**kwargs):
    for key, value in kwargs.items():
        print(f'key: {key}, value: {value}')

# Should print
# key: a, value: 12
# key: b, value: 30
_f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
_f4(city="Berkeley", population=121240, founded="March 23, 1868")

D = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the _f4 call below to make this work?
_f4(**D)
