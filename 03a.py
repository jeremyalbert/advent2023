# grep for anything that is not a period
# for diag for 3 numbers on line 21, position 18,19,20 look for their position in the string.
# Then check the line before and after to see if there is anything NOT a period from 17,18,19,20,21.
# Also check for not a period before or after the number.

# make a grid of each character on each line
grid = open('parts.txt').read().splitlines()

# store the coords of the first number in a set
coordset = set()

# enumerate the row and get index
# r = row coord
for rcord, row in enumerate(grid):
    # for character
    # ccord = column coord, ch = digit
    for ccord, foundchar in enumerate(row):
        # if char is anything but a digit or period (special character), continue
        if foundchar.isdigit() or foundchar == '.':
            # found a special character
            continue

        # if not a special character
        # scan around the character
        for currow in [rcord-1, rcord, rcord + 1]:
            for curcol in [ccord-1, ccord, ccord + 1]:
                # if the row or column is out of bounds or not a digit, continue
                if currow < 0 or currow >= len(grid) or curcol < 0 or curcol >= len(grid[currow]) or not grid[currow][curcol].isdigit():
                    continue

                # if the current column is greater than 0 and is digit, decrease the column by 1
                while curcol > 0 and grid[currow][curcol - 1].isdigit():
                    curcol -= 1

                # add the coord to the coordset
                coordset.add((currow, curcol))

#print(coordset)

# get numbers from coordset
numberlist = []

# for rows and columns in coordset, get the number from the grid and add it to the numberlist.
for rows, cols in coordset:
    # keeper string
    s = ""
    # while column is less than length of the row and the character is a digit, add the character to the string
    while cols < len(grid[rows]) and grid[rows][cols].isdigit():
        # add number to string
        s += grid[rows][cols]
        # increase by 1 to scan to right
        cols += 1

    # add the number to the numberlist
    numberlist.append(int(s))

# add the numbers in the numberlist together
print(sum(numberlist))
