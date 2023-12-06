import math
import re

# Get a list of cards.
# Each card is it's own line.
# if a number to the right of the | is in the left of the |, then it's a match and a winning number.
# Count all winning numbers for a total score.

# Game X: Winning numbers | My numbers

# matches = 5

# print (int(math.pow(2, matches -1)))

finalscore = 0

# open the file line by line
with open("cards.txt") as file:
    for line in file:
        winningnumbers = []
        matches = 0

        # to make splitting easier
        line = re.sub(":", "|", line)

        # Pull things from the line
        gameID = line.split("|")[0]
        #print(gameID)

        # Get the winning numbers
        winningnumbers = line.split("|")[1].lstrip().rstrip().strip()
        winningnumbers = winningnumbers.split(" ")
        winningnumbers = list(filter(None, winningnumbers))
        #print(winningnumbers)

        # Get the playing numbers
        playnum = line.split("|")[2].lstrip().rstrip().strip()
        playnum = playnum.split(" ")
        playnum = list(filter(None, playnum))
        #print(playnum)

        # Check to see if winning number is in play numbers
        for num in winningnumbers:
            if num in playnum:
                #print(f"Winning number {num} in play numbers")
                matches += 1
        #print (int(math.pow(2, matches -1)))
        finalscore += int(math.pow(2, matches -1))

print(finalscore)