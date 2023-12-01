import re

# open a file and read each line
# each line will have an integer or more
# take the first and last integer of each line
# if there is only one integer, add it to itself
# add them together

# array for coords
coords = []

# list to string
def list2string(l):
    return ''.join(map(str, l))

# get 2 digits
def get2digits(s):
    # get first and last digit from the string via slicing
    t = s[0] + s[-1]
    return t

# open the file line by line
with open("coords.txt") as file:
    for line in file:

        # use regex to get the integer(s)
        fullnumbers = re.findall("[0-9]+", line)

        # if there is only one integer, add it to itself
        if len(fullnumbers) == 1 and len(fullnumbers[0]) == 1:
            fullnumbers.append(int(fullnumbers[0]))

        # convert line list to string
        numstr = list2string(fullnumbers)

        # if the line is blank, skip it
        if len(numstr) == 0:
            continue

        # get first and last digit from each line
        elif len(numstr) != 2:
            # get first and last digit from the string via slicing
            numstr = get2digits(numstr)

        # append 2 digit coords
        coords.append(numstr)

coordsum = 0
for coord in coords:
    coordsum = coordsum + int(coord)

# print the coord result
print(coordsum)