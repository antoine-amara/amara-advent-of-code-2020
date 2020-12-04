def parse1DArrayToInt(filepath):
    parsedInput = []
    with open(filepath, "r+") as file:
        for line in file:
            parsedInput.append(int(line))
    return parsedInput
