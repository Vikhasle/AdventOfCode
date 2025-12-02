import numpy as np
import re
import sys

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines



def part_one(players, max_val):
    board = [0]
    last_ind = 0
    next_marb = 1
    scores = [0] * players
    rest = max_val % 23 - 1
    while True:
        if next_marb % 23 == 0:
            last_ind = (last_ind - 6) % len(board)
            scores[next_marb % players] += next_marb + board[last_ind]
            board.pop(last_ind)
            last_ind -= 1
        else:
            last_ind = (last_ind + 2) % len(board)
            board.insert(last_ind + 1, next_marb)
        next_marb += 1
        print(next_marb)
        if next_marb > max_val - rest:
            break

    return max(scores)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input1 = (411, 71170)
        input2 = (411, 71170 * 100)
    else:
        input1 = (10, 1618)
        input2 = (10, 1618 * 100)
    print("PartOne", part_one(*input1))
    print("PartTwo", part_one(*input2))
