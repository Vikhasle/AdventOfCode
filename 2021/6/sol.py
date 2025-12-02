from functools import cache
from math import log, floor


@cache
def repoduce(count, day, lim):
    if day == lim:
        return 1
    total = 0
    if count == 0:
        total += repoduce(9, day, lim)
        count = 7
    return total + repoduce(count-1, day + 1, lim)

def main():
    with open("input", "r") as file:
        fishes = list(map(int, file.readline().split(",")))
        c = 0
        for fish in fishes:
            c+= repoduce(fish, 0, 256)
        print(c)

if __name__ == "__main__":
    main()
