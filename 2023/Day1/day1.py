import numpy as np


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    sum = 0
    for line in input:
        for char in line:
            if char.isdigit():
                sum += int(char) * 10
                break
        for char in line[::-1]:
            if char.isdigit():
                sum += int(char)
                break
    return sum


def part_two(input):
    digits = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            ]
    sum = 0
    for line in input:
        first = (-1, "")
        last = (-1, "")
        for digit in digits:
            l_p = line.find(digit)
            r_p = line[::-1].find(digit[::-1])
            if l_p != -1:
                if first[0] == -1 or first[0] > l_p:
                    first = (l_p, digit)
            if r_p != -1:
                if last[0] == -1 or last[0] > r_p:
                    last = (r_p, digit)
        sum += 10 * (digits.index(first[1]) % 9 + 1) + digits.index(last[1]) % 9 + 1
    return sum


if __name__ == "__main__":
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
