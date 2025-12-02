import numpy as np

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        skip = lines[0].index(':') + 2
        lines = [x[skip:].strip() for x in lines]
        lines = [c.replace('  ', ' ') for c in lines]
        lines = [c.split(' ') for c in lines]
        div = lines[0].index('|')
        winning = [list(map(int, c[:div])) for c in lines]
        nums = [list(map(int, c[div + 1:])) for c in lines]
        return winning, nums


def num_matches(input):
    total = 0
    for num in input[0]:
        if num in input[1]:
            total += 1
    return total


def score(input):
    score = num_matches(input)
    return 0 if score == 0 else 2**(score - 1)


def part_one(winning, nums):
    return sum(map(score, zip(winning, nums)))


def part_two(w, n):
    copy_count = np.ones(len(w))
    total = 0
    for i, card in enumerate(zip(w, n)):
        score = num_matches(card)
        for j in range(score):
            copy_count[i + 1 + j] += copy_count[i]
        total += copy_count[i]
    return total


def main():
    w, n = get_input("input.txt")
    print("PartOne", part_one(w, n))
    print("PartTwo", part_two(w, n))


if __name__ == "__main__":
    main()
