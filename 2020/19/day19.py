class Tile:
    def __init__(self, id, map):
        self.id = id
        self.top = map[0]
        self.right = [x[len(map) - 1] for x in map]
        self.left = [x[0] for x in map]
        self.bottom = map[len(map) - 1]
        self.sides = [top, right, left, bottom]

    def rotate_cw(self):
        temp = self.bottom
        self.bottom, self.right = self.right, self.top
        self.top, self.left = self.left, temp

    def rotate_ccw(self):
        temp = self.bottom
        self.bottom, self.left = self.left, self.top
        self.top, self.right = self.right, temp

    def flip(self):
        self.top, self.bottom = self.bottom, self.top


def part_one(tiles):
    for i, tile in enumerate(tiles):
        matches = 0
        for j, tile2 in enumerate(tiles):
            for s in tile.sides:
                for s2 in tile2.sides:
                    if s == s2:
                        matches += 1
                        found = True
                        break
    return


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        i = 0
        tiles = []
        while i < len(lines):
            id = int(lines[i][5:9])
            map = []
            for j in range(i + 1, i + 10):
                map.append(lines[j].strip())
            tiles.append(Tile(id, map))
            i += 12
    part_one(tiles)


if __name__ == "__main__":
    main()
