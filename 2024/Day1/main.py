import numpy as np
from collections import Counter


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        r_list = [int(l.split("   ")[1]) for l in lines]
        l_list = [int(l.split("   ")[0]) for l in lines]
    return l_list, r_list


def part_one(l_list, r_list):
    l_list = np.array(sorted(l_list))
    r_list = np.array(sorted(r_list))
    l1_dist = np.linalg.norm(l_list - r_list, ord=1)
    return l1_dist


def part_two(l_list, r_list):
    counts = Counter(r_list)
    similiarity = 0
    for item in l_list:
        similiarity += item * counts[item]
    return similiarity


if __name__ == "__main__":
    l, r = get_input("input.txt")
    print("PartOne", part_one(l, r))
    print("PartTwo", part_two(l, r))
