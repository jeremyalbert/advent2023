import re

# open a file and read each line
# each line will have an integer or more
# take the first and last integer of each line
# if there is only one integer, add it to itself
# add them together
# if the line has "one" or "two", etc make that an integer as well

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

        # due to an oversight in the instructions, replace written numbers that share and end and beginning with another
        line = line.replace("oneight", "oneeight")
        line = line.replace("threeight", "threeeight")
        line = line.replace("fiveight", "fiveeight")
        line = line.replace("sevenine", "sevennine")
        line = line.replace("nineight", "nineeight")
        line = line.replace("twone", "twoone")
        line = line.replace("eightwo", "eighttwo")
        line = line.replace("eighthree", "eightthree")

        # use regex to get the integer(s) ... this time written ones as well
        fullnumbers = re.findall("[0-9]|one|two|three|four|five|six|seven|eight|nine", line)

        # best way I could find to make "one" into "1", etc
        for i in range(len(fullnumbers)):
            if fullnumbers[i] == "one":
                fullnumbers[i] = 1
            elif fullnumbers[i] == "two":
                fullnumbers[i] = 2
            elif fullnumbers[i] == "three":
                fullnumbers[i] = 3
            elif fullnumbers[i] == "four":
                fullnumbers[i] = 4
            elif fullnumbers[i] == "five":
                fullnumbers[i] = 5
            elif fullnumbers[i] == "six":
                fullnumbers[i] = 6
            elif fullnumbers[i] == "seven":
                fullnumbers[i] = 7
            elif fullnumbers[i] == "eight":
                fullnumbers[i] = 8
            elif fullnumbers[i] == "nine":
                fullnumbers[i] = 9

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