from collections import Counter
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
        # Split the input into "range" and "string"
        split = line.split(':')

        # Count the number of characters
        count = Counter(split[1])

        # Get range for the count
        countRange = split[0].split()[0].split('-')

        # Temp values to hold range of numbers
        t = range(int(countRange[0]), int(countRange[1])+1)
        
        # Check to see if character between the given range
        if(int(count[split[0][-1]]) in t ):
            print("Pass")
            # If it does, increase valid count
            num += 1
        else:
            print("Fail")

    # Return number of valid passwords
    return num

answer(content)