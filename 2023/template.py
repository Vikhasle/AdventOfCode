def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    return


def part_two(input):
    return


def main():
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))


if __name__ == "__main__":
    main()
