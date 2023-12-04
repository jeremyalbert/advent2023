# grep for anything that is not a period
# for diag for 3 numbers on line 21, position 18,19,20 look for their position in the string.
# Then check the line before and after to see if there is anything NOT a period from 17,18,19,20,21.
# Also check for not a period before or after the number.

# find if there are two numbers that touch a *

# make a grid of each character on each line
grid = open('parts.txt').read().splitlines()

# store gear ratio
ratio = 0

# enumerate the row and get index
# rcord = row coord
for rcord, row in enumerate(grid):
    # for character
    # ccord = column coord, ch = digit
    for ccord, foundchar in enumerate(row):
        # if the char is not a *
        if foundchar != "*":
            # found a special character
            continue

        # store the coords of the *
        coordset = set()

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

        # checking to see if there are two numbers that touch a *
        if len(coordset) != 2:
            continue

        # get numbers from coordset
        numberlist = []

        # for rows and columns in coordset, get the number from the grid and add it to the numberlist.
        for currow, curcol in coordset:
            # keeper string
            s = ""
            # while column is less than length of the row and the character is a digit, add the character to the string
            while curcol < len(grid[currow]) and grid[currow][curcol].isdigit():
                # add number to string
                s += grid[currow][curcol]
                # increase by 1 to scan to right
                curcol += 1

            # add the number to the numberlist
            numberlist.append(int(s))
            print(numberlist)

        # Get gear ratio and add them to the total
        ratio += numberlist[0] * numberlist[1]

print(ratio)