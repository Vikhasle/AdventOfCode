import numpy as np
import sys
import string

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    child_map = {}
    req_map = {}
    root = None
    for instruction in input:
        parent = instruction[5]
        child = instruction[36]
        if root is None:
            root = parent
        if parent not in child_map:
            child_map[parent] = [child]
        else:
            child_map[parent].append(child)
        if child not in req_map:
            req_map[child] = [parent]
        else:
            req_map[child].append(parent)

        if parent not in req_map:
            req_map[parent] = []

    stack = []
    route = ""
    for node in req_map:
        if req_map[node] == []:
            stack.append(node)
    while len(stack):
        stack.sort()
        curr_node = stack.pop(0)
        route += curr_node
        for node in req_map:
            if node in route or node in stack:
                continue
            elif all(map(lambda x: x in route, req_map[node])):
                stack.append(node)

    return route


def available_task(using, done, req_map):
    stack = []
    for node in req_map:
        if node in done or node in using:
            continue
        elif all(map(lambda x: x in done, req_map[node])):
            stack.append(node)
    stack.sort()
    return stack


def part_two(input):
    child_map = {}
    req_map = {}
    root = None
    for instruction in input:
        parent = instruction[5]
        child = instruction[36]
        if root is None:
            root = parent
        if parent not in child_map:
            child_map[parent] = [child]
        else:
            child_map[parent].append(child)
        if child not in req_map:
            req_map[child] = [parent]
        else:
            req_map[child].append(parent)

        if parent not in req_map:
            req_map[parent] = []

    done = ""
    num_workers = 5
    worker_timers = [0] * num_workers
    worker_tasks = ['.'] * num_workers
    steps = 0
    while True:
        for i, w_status in enumerate(worker_tasks):
            if w_status != '.':
                worker_timers[i] -= 1
                if worker_timers[i] == 0:
                    done += w_status
                    worker_tasks[i] = '.'
        tasks = available_task(worker_tasks, done, req_map)
        for i, w_status in enumerate(worker_tasks):
            if len(tasks) and w_status == '.':
                worker_tasks[i] = tasks.pop(0)
                worker_timers[i] = string.ascii_uppercase.index(worker_tasks[i]) + 61
        if all(map(lambda x: x == '.', worker_tasks)):
            break
        steps += 1
    return steps


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("input7.txt")
    else:
        input = get_input("test7.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
