def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x[x.find(":") + 1 :].strip() for x in file.readlines()]
        return lines


def part_one(input):
    max_cubes = {"blue": 14, "red": 12, "green": 13}
    impossible = []
    for game in input:
        i = 0
        while i < len(game):
            next = game[i:].find(", ")
            if next == -1 or game[i:].find("; ") != -1 and game[i:].find("; ") < next:
                next = game[i:].find("; ")
            if next == -1:
                next = len(game[i:])
            fields = game[i : next + i].split(" ")
            if max_cubes[fields[1]] < int(fields[0]):
                impossible.append(input.index(game) + 1)
                break
            i += next + 2
    return sum(range(1, len(input) + 1)) - sum(impossible)


def part_two(input):
    result = 0
    for game in input:
        max_cubes = {"blue": 0, "red": 0, "green": 0}
        i = 0
        while i < len(game):
            next = game[i:].find(", ")
            if next == -1 or game[i:].find("; ") != -1 and game[i:].find("; ") < next:
                next = game[i:].find("; ")
            if next == -1:
                next = len(game[i:])
            fields = game[i : next + i].split(" ")
            max_cubes[fields[1]] = max(max_cubes[fields[1]], int(fields[0]))
            i += next + 2
        result += max_cubes["blue"] * max_cubes["red"] * max_cubes["green"]
    return result


if __name__ == "__main__":
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
