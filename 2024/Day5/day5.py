from collections import defaultdict


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
    split = lines.index('')
    rules = lines[:split]
    data = lines[split+1:]
    return rules, data


def is_correct(nums, order):
    for i, num in enumerate(nums[:-1]):
        if any(map(lambda n: n in nums[i+1], order[num])):
            return False
    return True


def part_one(rules, data):
    order = defaultdict(list)
    for rule in rules:
        vals = rule.split('|')
        order[vals[1]].append(vals[0])
    total = 0
    for update in data:
        nums = update.split(',')
        if is_correct(nums, order):
            total += int(nums[len(nums) // 2])
    return total


def part_two(rules, data):
    order = defaultdict(list)
    for rule in rules:
        vals = rule.split('|')
        order[vals[1]].append(vals[0])
    total = 0
    for update in data:
        nums = update.split(',')
        if is_correct(nums, order):
            continue
        i = 0
        while i < len(nums) - 1:
            wrong = list(filter(lambda n: n in order[nums[i]],
                                nums[i+1:]))
            if len(wrong) == 0:
                i += 1
            else:
                j = nums.index(wrong[-1])
                nums[i], nums[j] = nums[j], nums[i]

        total += int(nums[len(nums) // 2])

    return total


if __name__ == "__main__":
    input = get_input("input")
    print("PartOne", part_one(*input))
    print("PartTwo", part_two(*input))
