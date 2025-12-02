from functools import reduce


def eval_add(exps):
    new_exps = [1]
    while "+" in exps:
        i = exps.index("+")
        rew = int(exps[i - 1]) + int(exps[i + 1])
        exps.pop(i - 1)
        exps.pop(i - 1)
        exps[i - 1] = rew

    for e in exps:
        if e != "*":
            new_exps.append(e)
    return new_exps


def eval_par(exps):
    while "(" in exps:
        start = exps.index("(")
        j = start
        c = 1
        while c > 0:
            j += 1
            if exps[j] == "(":
                c += 1
            elif exps[j] == ")":
                c -= 1
        exps[start] = eval(exps[start + 1 : j])

        for _ in range(start, j):
            exps.pop(start + 1)


def eval(exps):
    eval_par(exps)
    new = eval_add(exps)
    return reduce(lambda a, b: int(a) * int(b), new)


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    part_one = 0
    for line in lines:
        fields = line.strip()
        print(fields)
        fields = fields.replace(" ", "")
        fields = [x for x in fields]
        part_one += eval(fields)
    print(part_one)


if __name__ == "__main__":
    main()
