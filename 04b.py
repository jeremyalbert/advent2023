import re

# Get a list of cards.
# Each card is it's own line.
# if a number to the right of the | is in the left of the |, then it's a match and a winning number.
# Count all winning numbers for a total score.

# Game X: Winning numbers | My numbers

# open the file line by line
with open("cards.txt") as file:
    lines = file.read().strip().split("\n")

# get the number (games) of lines in the file
numlines = len(lines)

# holder for number of copies for each game
copies = [[] for z in range(numlines)]

# for each line
for i, line in enumerate(lines):
    # split line on spaces
    text = re.split("\s+", line)

    # split on |
    games = text.index("|")

    # get winning numbers
    winningnums = list(map(int, text[2:games]))

    # get my numbers
    mynums = list(map(int, text[games+1:]))

    score = 0

    # for each numbner in my numbers:
    for nums in mynums:
        # if it's in winning numbers, add 1 to score.
        if nums in winningnums:
            score += 1

    # add the amount of copies we need for each to our copies list
    for x in range(i + 1, i + score + 1):
        copies[i].append(x)

    score = [1 for y in range(numlines)]

    # reverse loop through the games and then add the number of games to the score
    for i in range(numlines -1, -1, -1):
        for j in copies[i]:
            score[i] += score[j]

print(sum(score))
