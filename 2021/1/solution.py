
def part_one():
    file = open("input", "r")
    ints = list(map(int, file.readlines()))
    j = -1
    count = 0
    for i in ints:
        if i > j:
            count +=1
        j = i
    print(count)

def part_two():
    file = open("input", "r")
    ints = list(map(int, file.readlines()))
    count = 0
    window = ints[:3]
    for i in ints[3:]:
        if i > window.pop(0):
            count+=1
        window.append(i)
    print(count)

part_two()
