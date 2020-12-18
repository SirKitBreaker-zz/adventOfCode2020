with open("input.txt", "r") as f:
    content = f.readlines()
    # remove whitespace characters like '\n' at the end of each line
    # and save it as a list
content = [x.strip() for x in content]

for line in content:
    line = line * 10
    print(line)