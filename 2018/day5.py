import numpy as np
import string

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines[0]


def part_one(input):
    curr_str = input
    last_len = 0
    while last_len != len(curr_str):
        i = 0
        last_len = len(curr_str)
        while i < len(curr_str) - 1:
            if curr_str[i] != curr_str[i+1] and (curr_str[i] == curr_str[i+1].upper() 
                                                 or curr_str[i] == curr_str[i+1].lower()):
                curr_str = curr_str.replace(curr_str[i:i+2], "")
            i += 1

    return len(curr_str)


def part_two(input):
    curr_min = np.inf
    for c in string.ascii_lowercase:
        if c in input:
            removed = input.replace(c, "").replace(c.upper(), "")
            result = part_one(removed)
            curr_min = min(result, curr_min)
    return curr_min


if __name__ == "__main__":
    input = get_input("input5.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
