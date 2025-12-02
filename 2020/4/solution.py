import re


def read_inp():
    fil = open("/home/kre213/Koding/AdventOfCode/2020/4/input",
               "r").read().split("\n\n")
    return fil


def part_one(inp):
    fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]

    valid = 0

    for port in inp:
        i = True
        for field in fields:
            if field+":" not in port:
                i = False
                break
        if i:
            valid += 1

    return valid


def part_two(inp):
    fields = {
        "byr": r"byr:(19[2-9]\d|200[0-2])\b",
        "iyr": r"iyr:20(1\d|20)\b",
        "eyr": r"eyr:20(2\d|30)\b",
        "hgt": r"hgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)\b",
        "hcl": r"hcl:#[a-f0-9]{6}\b",
        "ecl": r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b",
        "pid": r"pid:\d{9}\b"
    }
    valid = 0
    for port in inp:
        i = True
        for field in fields:
            if re.search(fields[field], port) == None:
                i = False
                break
        if i:
            valid += 1

    return valid


test = [
    "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
    "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"
]
print(part_one(read_inp()))
print(part_two(read_inp()))
