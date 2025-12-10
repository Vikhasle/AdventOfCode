import numpy as np
from scipy.optimize import nnls, milp, Bounds, LinearConstraint
import re
from itertools import combinations
import sys


class Indicator:
    def __init__(self, lights):
        self.goal = set()
        self.state = set()
        for i in range(len(lights)):
            if lights[i] == '#':
                self.goal.add(i)

    def dist(self):
        return sum(self.goal - self.state)

    def reset(self):
        self.state = set()

    def push(self, but):
        self.state = self.state ^ but

    def push_all(self, seq):
        self.reset()
        for b in seq:
            self.push(b)
        return self.state == self.goal


def min_presses(m, buttons):
    for k in range(1, len(buttons)):
        seqs = combinations(buttons, k)
        for seq in seqs:
            if m.push_all(seq):
                return k
    return -1  # Unable to solve


def to_vector(button, n):
    vec = [0] * n
    for i in button:
        vec[i] = 1
    return vec


def part_one(input):
    total = 0
    for m_desc in input:
        ind_lights = re.search(r"\[.*\]", m_desc)
        joltages = re.search(r"\{.*\}", m_desc)
        buttons = m_desc[ind_lights.end()+1: joltages.start()-1].split(' ')
        buttons = [set(map(int, x[1:-1].split(','))) for x in buttons]
        m = Indicator(ind_lights[0][1:-1])
        total += min_presses(m, buttons)

    return total


def solve(a, b):
    n = a.shape[1]
    c = np.ones(n)
    b_eq = b
    constraints = LinearConstraint(A=a, lb=b_eq, ub=b_eq),
    milp_bounds = Bounds(lb=0, ub=np.inf)
    integrality=[1]*n

    result = milp(c, integrality=integrality, constraints=constraints, bounds=milp_bounds)
    return np.round(result.x).astype(int)


def part_two(input):
    total = 0
    for m_desc in input:
        ind_lights = re.search(r"\[.*\]", m_desc)
        joltages = re.search(r"\{.*\}", m_desc)
        buttons = m_desc[ind_lights.end()+1: joltages.start()-1].split(' ')
        buttons = [set(map(int, x[1:-1].split(','))) for x in buttons]
        levels = tuple(map(int, joltages[0][1:-1].split(',')))
        n = len(levels)
        goal = [0] * n
        for i in range(len(levels)):
            goal[i] = levels[i]
        a = np.array([to_vector(but, n) for but in buttons], dtype=np.uint64)
        b = np.array(goal, dtype=np.uint64)
        total += sum(solve(a.T, b))

    return total


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day10")
    else:
        input = get_input("tests/test10")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
