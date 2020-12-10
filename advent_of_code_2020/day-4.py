print("########## DAY 4 ##########")


def parseDay4(input_path):
    allPassports = []
    parsedLine = {}
    with open(input_path, "r+") as file:
        for line in file:
            if line == "\n":
                allPassports.append(parsedLine)
                parsedLine = {}
            else:
                cleanLine = line.rstrip()
                for element in cleanLine.split(" "):
                    key, value = element.split(":")
                    parsedLine[key] = value
    allPassports.append(parsedLine)
    return allPassports


def checkPassports_part1(passports):
    requiredKeys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    return sum([set(requiredKeys).issubset(passport) for passport in passports])


def checkOnePassportPart2(onePassport):
    requiredKeys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    if not (set(requiredKeys).issubset(onePassport)):
        return False
    else:
        if not (int(onePassport["byr"]) >= 1920 and int(onePassport["byr"]) <= 2002):
            return False
        if not (int(onePassport["iyr"]) >= 2010 and int(onePassport["byr"]) <= 2020):
            return False
        if not (int(onePassport["eyr"]) >= 2020 and int(onePassport["byr"]) <= 2030):
            return False
        if not (onePassport["hcl"][0] == "#" and onePassport["hcl"][1:].isalnum()):
            return False
        if not (
            onePassport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        ):
            return False
        if len(onePassport["pid"]) != 9:
            return False

        hgt = onePassport["hgt"][:-2]
        if not hgt:
            return False
        if onePassport["hgt"][-2:] == "cm":
            if not (int(hgt) >= 150 and int(hgt) <= 193):
                return False
        if onePassport["hgt"][-2:] == "in":
            if not (int(hgt) >= 59 and int(hgt) <= 76):
                return False

        return True


def checkPassports_part2(passports):
    allPassportValidation = [checkOnePassportPart2(passport) for passport in passports]
    return sum(allPassportValidation)


def day4(validationPassportFunc):
    allParsedPassports = parseDay4("advent_of_code_2020/inputs/day4.txt")
    return validationPassportFunc(allParsedPassports)


number_of_valid_passport_part1 = day4(checkPassports_part1)
print(number_of_valid_passport_part1)
number_of_valid_passport_part2 = day4(checkPassports_part2)
print(number_of_valid_passport_part2)
