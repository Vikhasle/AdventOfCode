import numpy as np
import sys


def get_input(file_name):
    with open(file_name, "r") as file:
        sections = file.read().split('\n\n')
        regions = sections[-1].split('\n')
        regions = [reg.split(': ') for reg in regions][:-1]
        regions = [reg[0].split('x') + reg[1].split(' ') for reg in regions]
        regions = [list(map(int, reg)) for reg in regions]
        regions = [(reg[0], reg[1], reg[2:]) for reg in regions]
        shapes = sections[:-1]
        shapes = [Shape(shape.split('\n')[1:]) for shape in shapes]
        return shapes, regions


class Shape:
    def __init__(self, shape_str):
        self.shape = [list(map(lambda x: 1 if x == '#' else 0, l)) for l in shape_str]
        self.shape = np.array(self.shape)

    def shape(self):
        return self.shape.shape

    def perms(self):
        all_perms = [self.shape]
        for k in range(1, 4):
            all_perms.append(np.rot90(self.shape, k))
        all_perms.append(np.fliplr(self.shape))
        all_perms.append(np.flipud(self.shape))

        return all_perms


def part_one(shapes, regions):
    valids = 0

    for (n, m, counts) in regions:
        canvas = n * m
        total = 0

        for i, c in enumerate(counts):
            total += c * (shapes[i].shape.shape[0] * shapes[i].shape.shape[1])

        if total <= canvas:
            valids += 1
    return valids

def part_two(shapes, regions):
    return

if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day12")
    else:
        input = get_input("tests/test12")
    print("PartOne", part_one(*input))
    print("PartTwo", part_two(*input))
