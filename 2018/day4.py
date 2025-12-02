import re
import numpy as np

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def sum_time(logs):
    total = 0
    for day in logs:
        total += day.count("#")

    return total


def key_dates(d1):
    key_d1 = int(d1[1:5] + d1[6:8] + d1[9:11] + d1[12:14] + d1[15:17])
    return key_d1


def part_one(input):
    input = sorted(input, key=key_dates)
    guard_timers = {}
    time_stamp = re.compile(":[0-9][0-9]")
    guard_match = re.compile("Guard #[0-9]+")
    curr_guard = guard_match.search(input[0]).group()
    guard_timers[curr_guard] = ["."*60]
    sleep_start = None
    for line in input[1:]:
        if "asleep" in line:
            sleep_start = int(time_stamp.search(line).group()[1:])
        elif "wakes" in line:
            curr_time = int(time_stamp.search(line).group()[1:])
            curr_sleep = guard_timers[curr_guard][-1]
            guard_timers[curr_guard][-1] = curr_sleep[:sleep_start] + \
                "#" * (curr_time - sleep_start) + curr_sleep[curr_time:]
        else:
            curr_guard = guard_match.search(line).group()
            if curr_guard not in guard_timers:
                guard_timers[curr_guard] = ["."*60]
            else:
                guard_timers[curr_guard].append("."*60)
    times = [(g, sum_time(guard_timers[g])) for g in guard_timers]
    max_guard = max(times, key=lambda x: x[1])

    
    indices_count = [0 for i in range(60)]
    for date in guard_timers[max_guard[0]]:
        for i, minute in enumerate(date):
            if minute == '#':
                indices_count[i] += 1
    guard_nr = int(max_guard[0][max_guard[0].index("#") + 1:])
    return np.argmax(indices_count) * guard_nr


def part_two(input):
    input = sorted(input, key=key_dates)
    guard_timers = {}
    time_stamp = re.compile(":[0-9][0-9]")
    guard_match = re.compile("Guard #[0-9]+")
    curr_guard = guard_match.search(input[0]).group()
    guard_timers[curr_guard] = ["."*60]
    sleep_start = None
    for line in input[1:]:
        if "asleep" in line:
            sleep_start = int(time_stamp.search(line).group()[1:])
        elif "wakes" in line:
            curr_time = int(time_stamp.search(line).group()[1:])
            curr_sleep = guard_timers[curr_guard][-1]
            guard_timers[curr_guard][-1] = curr_sleep[:sleep_start] + \
                "#" * (curr_time - sleep_start) + curr_sleep[curr_time:]
        else:
            curr_guard = guard_match.search(line).group()
            if curr_guard not in guard_timers:
                guard_timers[curr_guard] = ["."*60]
            else:
                guard_timers[curr_guard].append("."*60)
    max_times = 0
    max_minute = 0
    guard_nr = 0
    for g in guard_timers:
        indices_count = [0 for i in range(60)]
        for date in guard_timers[g]:
            for i, minute in enumerate(date):
                if minute == '#':
                    indices_count[i] += 1
        if max(indices_count) > max_times:
            max_minute = np.argmax(indices_count)
            guard_nr = int(g[g.index("#") + 1:])
            max_times = max(indices_count)
    return max_minute * guard_nr


if __name__ == "__main__":
    input = get_input("test4.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
