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

waypoints = [
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
waypoints.append({"lat": 28, "lon": -122, "name": "a fourth place"})

print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
waypoints[0]['lon'] = -130
print(waypoints[0])

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

# initialize count variables
count = 1

for place in waypoints:
    # waypoint labels
    if count == 1:
        print(f'{count}st waypoint:')
    elif count == 2:
        print(f'{count}nd waypoint:')
    elif count == 3:
        print(f'{count}rd waypoint:')
    else:
        print(f'{count}th waypoint:')

    # increment count
    count = count + 1

    # loop and print dict fields
    for key in place:
        print(f'{key}: {place[key]}')
