from advent_of_code_2020.helpers import fileparsers

print("########## DAY 1 ##########")

# find 2 elements a and b which they're sum are equal to 2020
# finaly return a * b
# find 3 elements for part 2

# example = [1721, 979, 366, 299, 675, 1456]
# part 1: a=1721 b=299 response=514579
# part 2: a=979 b=366 c=675 response=241861950


def day1_part1(inputs):
    for current_input in inputs:
        if (2020 % current_input) in inputs:
            return (2020 % current_input) * current_input


def day1_part2(inputs):
    for first_input in inputs:
        for second_input in inputs:
            if (2020 % first_input + second_input) in inputs:
                return (2020 % first_input + second_input) * first_input * second_input


inputs = fileparsers.parse1DArrayToInt("advent_of_code_2020/inputs/day1.txt")
print(inputs)
part1 = day1_part1(inputs)
print("part1:")
print(part1)
part2 = day1_part2(inputs)
print("part2:")
print(part2)