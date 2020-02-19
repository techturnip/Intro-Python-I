"""
Write a program to determine if a number, given on the command line, is prime
"""
import sys

ARGS = [arg for arg in sys.argv[1:]]

NUM_OF_ARGS = len(ARGS)

def prime_sieve(_n):
    """takes a num and returns true or false if is prime"""
    if _n > 5:

        for e in range(2, _n//2):

            if _n % e == 0:
                return False
            else:
                return True
    else:
        return False

if not NUM_OF_ARGS:
    sys.exit("Please pass a number from the commandline")
elif NUM_OF_ARGS > 1:
    sys.exit("Please pass only 1 number from the commandline")
else:
    print(prime_sieve(int(ARGS[0])))
