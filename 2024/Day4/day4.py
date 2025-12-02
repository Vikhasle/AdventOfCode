
def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def check(input, i, j):
    xmas_count = 0

    if j - 3 >= 0:
        xmas_count += input[i][j-3:j+1] == "SAMX"
    if j + 3 < len(input[0]):
        xmas_count += input[i][j:j+4] == "XMAS"

    if i + 3 < len(input):
        sub_str = [l[j] for l in input[i:i+4]]
        xmas_count += "".join(sub_str) == "XMAS"
    if i - 3 >= 0:
        sub_str = [l[j] for l in input[i-3:i+1]]
        xmas_count += "".join(sub_str) == "SAMX"

    if i + 3 < len(input) and j + 3 < len(input[0]):
        sub_str = [input[i+k][j+k] for k in range(4)]
        xmas_count += "".join(sub_str) == "XMAS"
    if i + 3 < len(input) and j - 3 >= 0:
        sub_str = [input[i+k][j - k] for k in range(4)]
        xmas_count += "".join(sub_str) == "XMAS"
    if i - 3 >= 0 and j + 3 < len(input[0]):
        sub_str = [input[i-k][j + k] for k in range(4)]
        xmas_count += "".join(sub_str) == "XMAS"
    if i - 3 >= 0 and j - 3 >= 0:
        sub_str = [input[i-k][j - k] for k in range(4)]
        xmas_count += "".join(sub_str) == "XMAS"
    return xmas_count


def part_one(input):
    total = 0
    for i, l in enumerate(input):
        for j, c in enumerate(l):
            if c == 'X':
                total += check(input, i, j)
    return total

def check2(input, i, j):
    count = 0
    if i + 2 < len(input) and j + 2 < len(input[0]):
        sub_str = "".join([input[i+k][j+k] for k in range(3)])
        if sub_str == "MAS" or sub_str == "SAM":
            sub_str = "".join([input[i + 2 - k][j+k] for k in range(3)])
            count += sub_str == "MAS" or sub_str == "SAM"
    return count


def part_two(input):
    total = 0
    for i, l in enumerate(input):
        for j, c in enumerate(l):
            if c == 'M' or c == 'S':
                total += check2(input, i, j)
    return total


def main():
    input = get_input("input")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))


if __name__ == "__main__":
    main()
