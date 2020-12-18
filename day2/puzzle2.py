import re

# Open file with input numbers
with open("input.txt", "r") as f:
    content = f.readlines()
    # remove whitespace characters like '\n' at the end of each line
    # and save it as a list
content = [x.strip() for x in content]

def answer(input):
    # Number of valid passwords
    num = 0

    # Go through the input line by line
    for line in content:
        # Split the input into "positions" and "string"
        split = line.split(':')

        # Get character to find
        char = split[0][-1]

        # Get character positions
        charPositions = split[0].split()[0].split('-')

        # Find characters are given positions
        firstCharAt = split[1][int(charPositions[0])]
        secondCharAt = split[1][int(charPositions[1])]

        # Check if characters exist at both positions
        if(firstCharAt == secondCharAt):
            # If they do, the password is invalid
            print("Fail")
        # Otherwise, the character should be at any one of the positions
        elif((firstCharAt == char) | (secondCharAt == char)):
            print("Pass")
            # If it is, increase valid password count
            num += 1

    # Return count of valid passwords
    return num

answer(content)