"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# GRAB COMMANDLINE ARGS
ARGS = [ARG for ARG in sys.argv[1:]]
# CREATE CALENDAR OBJECT
CAL = calendar.TextCalendar(calendar.SUNDAY)
# GRAB TODAY'S DATE
TODAY = datetime.now()


# Sort list to ensure index order
def arg_len(single_arg):
    """Function returns the length of the string argument"""
    return len(single_arg)

# Use arg_len() as the key for sorting ARGS list by str length
ARGS.sort(key=arg_len)

# Pull out ARGS length for conditional
NUM_OF_ARGS = len(ARGS)

if NUM_OF_ARGS > 0:
    MONTH = int(ARGS[0])

if NUM_OF_ARGS > 1:
    YEAR = int(ARGS[1])

# Conditional logic to determine the value of global CAL_STR variable to print to console
if ARGS:
    # Check the length of the args array
    if NUM_OF_ARGS == 1:
        # Check for a valid month
        if 0 < MONTH <= 12:
            CAL_STR = CAL.formatmonth(TODAY.year, MONTH)
            print(CAL_STR)
        # Else print an error and instructions
        else:
            sys.exit("Invalid month: Please enter a valid month integer")
    elif NUM_OF_ARGS == 2:
        # Check for invalid month
        if MONTH < 1 or MONTH > 12:
            sys.exit("Invalid month: Please enter a valid month integer")
        # Check for invalid year
        elif len(ARGS[1]) != 4:
            sys.exit("Invalid year: Please enter a valid 4 digit year")
        # Else print calendar
        else:
            CAL_STR = CAL.formatmonth(YEAR, MONTH)
            print(CAL_STR)
    else:
        sys.exit("Too many arguments: Please enter valid 2 digit month and 4 digit year")
elif not ARGS:
    # Default cal if no ARGS
    CAL_STR = CAL.formatmonth(TODAY.year, TODAY.month)
    print(CAL_STR)
