import re
# figure out which games have less than 12 red cubes, 13 green, and 14 blue.
# if game matches, then put the game IDs into an array.
# add the IDs from the array together.

# Game 100: 5 green, 1 red; 4 blue, 8 red, 4 green; 1 blue, 3 red, 15 green; 1 blue, 15 green, 1 red; 2 red, 13 green

badgame = []
games = []
gameIDsum = []

# open the file line by line
with open("game.txt") as file:
    for line in file:

        # 4 splits, first to get the game ID, split on : (colon)
        gameID = line.split(":")[0]
        gameID = int(gameID.split(" ")[1])
        games.append(gameID)

        # Next split, get first set of cubes, split on ; (semicolon)
        line = re.sub(r"Game \d+: ", "", line)
        fullgame = line.split("; ")

        # Next split, split on , (comma)
        for gameset in fullgame:

            # reset colors
            red, green, blue = 0, 0, 0

            # Next split, split on (space)
            # figure out which color has which number
            itemset = gameset.split(", ")

            for i in itemset:
                i = i.rstrip()
                number, color = i.split(" ")
                number = int(number)

                if color == "red":
                    red += number
                    if red > 12:
                        #print(f"GameID bad: {gameID}")
                        badgame.append(gameID)

                elif color == "green":
                    green += number
                    if green > 13:
                        #print(f"GameID bad: {gameID}")
                        badgame.append(gameID)

                elif color == "blue":
                    blue += number
                    if blue > 14:
                        #print(f"GameID bad: {gameID}")
                        badgame.append(gameID)

gameIDsum.append(badgame)
# debugging
#print(list(set(badgame)))
#print(len(list(set(gameIDsum))))

win = []

for element in games:
    if element not in badgame:
        win.append(element)

gamesum = 0
for element in win:
    gamesum = gamesum + int(element)

print(gamesum)