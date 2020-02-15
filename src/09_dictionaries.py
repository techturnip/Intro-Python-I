"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

WAYPOINTS = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
WAYPOINTS.append({"lat": 28, "lon": -122, "name": "a fourth place"})

print(WAYPOINTS)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# WAYPOINTS list.

# YOUR CODE HERE
WAYPOINTS[0]['lon'] = -130
print(WAYPOINTS[0])

# Write a loop that prints out all the field values for all the WAYPOINTS
# YOUR CODE HERE

# initialize COUNT variables
COUNT = 1

for place in WAYPOINTS:
    # waypoint labels
    if COUNT == 1:
        print(f'{COUNT}st waypoint:')
    elif COUNT == 2:
        print(f'{COUNT}nd waypoint:')
    elif COUNT == 3:
        print(f'{COUNT}rd waypoint:')
    else:
        print(f'{COUNT}th waypoint:')

    # increment COUNT
    COUNT = COUNT + 1

    # loop and print dict fields
    for key in place:
        print(f'{key}: {place[key]}')
