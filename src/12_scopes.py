"""
Experiment with scopes in Python.
Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables
"""
# When you use a variable in a function, it's local in scope to the function.
X = 12

def change_x():
    """Change the global value of x inside func"""
    global X # pylint: disable=global-statement
    X = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(X)


# This nested function has a similar problem.

def _outer():
    _y = 120

    def _inner():
        nonlocal _y # using nonlocal keyword
        _y = 999

    _inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(_y)


_outer()
