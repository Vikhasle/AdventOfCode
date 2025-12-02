def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        lines = [list(map(int, line.split(' '))) for line in lines]
        return lines


def is_safe(rep):
    inc = True if rep[1] - rep[0] > 0 else False
    for i, lvl in enumerate(rep[:-1]):
        diff = rep[i + 1] - lvl
        if not 1 <= abs(diff) <= 3:
            return 0
        if diff < 0 and inc:
            return 0
        if diff > 0 and not inc:
            return 0
    return 1


def is_safe2(rep):
    inc = True if rep[1] - rep[0] > 0 else False
    for i, lvl in enumerate(rep[:-1]):
        diff = rep[i + 1] - lvl
        if (not 1 <= abs(diff) <= 3) or (diff < 0 and inc) or (diff > 0 and not inc):
            for j in range(i+2):
                sub_l = rep[:j] + ([] if j == len(rep) - 1 else rep[j+1:])
                print(sub_l)
                if is_safe(sub_l):
                    return 1
            return 0
    return 1


def part_one(input):
    return sum(map(is_safe, input))


def part_two(input):
    return sum(map(is_safe2, input))


def main():
    input = get_input("input")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))


if __name__ == "__main__":
    main()
