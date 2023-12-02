import re
# figure out the highest number of red, blue, and green for each game.
# multiple those numbers together and add to a list.
# then add all the numbers in the list together.

powersum = []

# open the file line by line
with open("game.txt") as file:
    for line in file:

        # 4 splits, first to get the game ID, split on : (colon)
        gameID = line.split(":")[0]
        gameID = int(gameID.split(" ")[1])

        # Next split, get first set of cubes, split on ; (semicolon)
        line = re.sub(r"Game \d+: ", "", line)
        fullgame = line.split("; ")

        # reset highest numbers
        holdr, holdg, holdb = 0, 0, 0

        # Next split, split on , (comma)
        for gameset in fullgame:

            # reset color numbers
            red, green, blue = 0, 0, 0

            # Next split, split on (space)
            # figure out which color has which number
            itemset = gameset.split(", ")

            for i in itemset:
                # remove trailing newline characters
                i = i.rstrip()
                number, color = i.split(" ")
                number = int(number)

                if color == "red":
                    red += number
                    if red >= holdr:
                        holdr = red

                elif color == "green":
                    green += number
                    if green >= holdg:
                        holdg = green

                elif color == "blue":
                    blue += number
                    if blue >= holdb:
                        holdb = blue

        # debugging
        #print(f"GameID: {gameID} Red: {red}, Green: {green}, Blue: {blue}")
        #print(f"GameID: {gameID} Hred: {holdr}, Hgreen: {holdg}, Hblue: {holdb}")

        # append each set of highest number from each game together in a list
        powersum.append(holdr * holdg * holdb)

# debugging
#print(powersum)
#print(len(powersum))

# add the numbers together
gamesum = 0
for element in powersum:
    gamesum = gamesum + int(element)

print(gamesum)