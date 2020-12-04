def parse1DArrayToInt(filepath):
    parsedInput = []
    with open(filepath, "r+") as file:
        for line in file:
            parsedInput.append(int(line))
    return parsedInput


def parse2DArrayToString(filepath, separator=","):
    parsedInput = []
    with open(filepath, "r+") as file:
        for line in file:
            parsedInput.append(line.split(separator))
    return parsedInput