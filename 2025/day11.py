import numpy as np
import re
import sys


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def dfs(node, end, graph, known):
    if node == end:
        return 1
    if node == "out":
        return 0
    if node in known:
        return known[node]
    paths = 0
    for edge in graph[node]:
        paths += dfs(edge, end, graph, known)
    known[node] = paths
    return paths


def part_one(input):
    graph = {}
    for line in input:
        vertex, edges = line.split(': ')
        graph[vertex] = [e for e in edges.split(' ')]

    return dfs("you", "out", graph, {})


def part_two(input):
    graph = {}
    for line in input:
        vertex, edges = line.split(': ')
        graph[vertex] = [e for e in edges.split(' ')]
    fft_first = dfs("svr", "fft", graph, {}) * dfs("fft", "dac", graph, {}) * dfs("dac", "out", graph, {})
    dac_first = dfs("svr", "dac", graph, {}) * dfs("dac", "fft", graph, {}) * dfs("fft", "out", graph, {})
    return fft_first + dac_first


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day11")
    else:
        input = get_input("tests/test11")
    #print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
