from itertools import combinations
from functools import reduce
from operator import mul

# Function to get Puzzle 1's answer
def answer():
    # Open file with input
    with open("input.txt", "r") as f:
        content = f.readlines()
        # remove whitespace characters like `\n` at the end of each line
        # and save it as a list of numbers
    content = [int(x.strip()) for x in content]

    # Iterate through list
    for s in combinations(content, 2):
        # Find the numbers that add up to 2020
        if sum(s) == 2020:
            # Multiply them
            return reduce(mul, s)

# Print the answer
print(answer())