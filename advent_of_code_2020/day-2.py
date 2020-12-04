from advent_of_code_2020.helpers import fileparsers

print("########## DAY 2 ##########")
# parse and return the number of valid password
# part 1: count occurence , should should between min-max element
# part 2: check if char is present at index N-M it should not appear twice
# exampleRawInputs = [
#     ["1-3", "a:", "abcde"],
#     ["1-3", "b:", "cdefg"],
#     ["1-3", "c:", "ccccccccc"],
# ]


# specific parser for this problem, it take as input a array of array of string
# from the parse input file
def parseDay2Inputs(rawInputs):
    parsedData = []
    for data in rawInputs:
        min_max_occurence = [int(n) for n in data[0].split("-")]
        character = data[1][0]
        str = data[2]
        parsedData.append(
            {"min_max_occurence": min_max_occurence, "character": character, "str": str}
        )
    return parsedData


# check validity of one password for part 1
def isValidStringOccurence(min_max_occurence, character, str):
    occurence = str.count(character)
    return occurence >= min_max_occurence[0] and occurence <= min_max_occurence[1]


# check validity of one password for part 2
def isValidStringCharPositions(first_second_index, character, str):
    first_index = first_second_index[0]
    second_index = first_second_index[1]
    if (str[first_index - 1] == character) and (str[second_index - 1] != character):
        return True
    if (str[first_index - 1] != character) and (str[second_index - 1] == character):
        return True

    return False


# return the number of valid password, it take the input from file
# and a function to valid one password
def day2(parsedInputs, passwordValidatorFunc):
    # return an array of boolean representing the validity of each password
    validArray = [
        passwordValidatorFunc(data["min_max_occurence"], data["character"], data["str"])
        for data in parsedInputs
    ]
    # return the number of True in the validArray
    return sum(validArray)


rawPart1Inputs = parseDay2Inputs(
    fileparsers.parse2DArrayToString("advent_of_code_2020/inputs/day2.txt", " ")
)

# Part 1
numberOfValidPasswordPart1 = day2(rawPart1Inputs, isValidStringOccurence)
print(numberOfValidPasswordPart1)

# Part 2
numberOfValidPasswordPart2 = day2(rawPart1Inputs, isValidStringCharPositions)
print(numberOfValidPasswordPart2)
