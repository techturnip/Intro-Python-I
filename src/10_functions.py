""" Write a function is_even that will return true if the passed-in number is even. """

# YOUR CODE HERE
def is_even(_n):
    """Function that returns True or False if n is even"""
    if _n % 2 == 0:
        return True
    return False



# Read a number from the keyboard
NUM = input("Enter a number: ")
NUM = int(NUM)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if is_even(NUM):
    print("Even!")
else:
    print("Odd")
