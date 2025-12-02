from math import log10

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        fields = [list(map(lambda x: int(x.strip(':')), a.split(' '))) for a in lines]
        return fields

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def cat(a, b):
    return 10 ** (int(log10(b)) + 1) * a + b


def check_sol(goal, nums, ops):
    curr_total = nums[0]
    i = 1
    for op in ops:
        curr_total = op(curr_total, nums[i])
        if curr_total > goal:
            return False
        i += 1
    return curr_total == goal


def part_one(input):
    total = 0
    for eq in input:
        goal = eq[0]
        nums = eq[1:]
        perms = [[]]
        for i in range(len(nums) - 1):
            # 2 ** N perms
            perms = [p + [add] for p in perms] + [p + [mul] for p in perms]
        for ops in perms:
            if check_sol(goal, nums, ops):
                total += goal
                break
    return total


def part_two(input):
    total = 0
    for eq in input:
        goal = eq[0]
        nums = eq[1:]
        perms = [[]]
        for i in range(len(nums) - 1):
            # 3 ** N perms
            perms = [p + [add] for p in perms] + [p + [mul] for p in perms] + [p + [cat] for p in perms]
        for ops in perms:
            if check_sol(goal, nums, ops):
                total += goal
                break
    return total


if __name__ == "__main__":
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
