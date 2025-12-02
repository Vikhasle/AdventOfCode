import re

def get_input(file_name):
    with open(file_name, "r") as file:
        return file.read()


def part_one(input):
    inst_expr = re.compile(r"mul\([0-9]+,[0-9]+\)")
    i = 0
    total = 0
    while match := inst_expr.search(input[i:]):
        split = match.group().index(',')
        m1 = match.group()[4:split]
        m2 = match.group()[split+1:-1]
        total += int(m1) * int(m2)
        i += match.end()
    return total


def part_two(input):
    inst_expr = re.compile(r"mul\([0-9]+,[0-9]+\)")
    do_expr = re.compile(r"do\(\)")
    dont_expr = re.compile(r"don't\(\)")
    enabled = True
    total = 0
    i = 0
    while match := inst_expr.search(input[i:]):
        dont_match = dont_expr.search(input[i:i+match.start()])
        do_match = do_expr.search(input[i:i+match.start()])
        if do_match and dont_match:
            enabled = True if do_match.start() > dont_match.start() else False
        elif dont_match:
            enabled = False
        elif do_match:
            enabled = True
        if enabled:
            split = match.group().index(',')
            m1 = match.group()[4:split]
            m2 = match.group()[split+1:-1]
            total += int(m1) * int(m2)
        i += match.end()
    return total


def main():
    input = get_input("input")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))


if __name__ == "__main__":
    main()
