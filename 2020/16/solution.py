def read_inp(filename: str):
    fil = open(filename, "r").read().split("\n\n")
    rules = fil[0].split('\n')
    rules_dict = {}
    for line in rules:
        n = line.split(":")
        b = [x.split('-') for x in n[1].split(" or ")]
        c = [(int(x[0]), int(x[1])) for x in b]
        rules_dict[n[0]] = c
    ticket = fil[1].split('\n')[1]
    ticket = [int(x) for x in ticket.split(",")]
    nearby = fil[2].split('\n')[1:]
    nearby = [x.split(',')for x in nearby]
    nearby = [[int(x) for x in b]for b in nearby]
    return rules_dict, ticket, nearby


def part_one(rules, nearby):
    values = 0
    for line in nearby:
        for val in line:
            valid = False
            for r in rules.values():
                valid = False
                for b in r:
                    if b[0] < val < b[1]:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                values += val
    return values


def remove_invalid(rules, nearby):
    i = 0
    while i < len(nearby):
        ticket = nearby[i]
        valid = True
        for val in ticket:
            f_func = lambda r: (r[0][0] <= val <= r[0][1]) or \
                            (r[1][0] <= val <= r[1][1])
            if not any(map(f_func, rules.values())):
                valid = False
        if valid:
            i += 1
        else:
            nearby.pop(i)
    return nearby


def part_two(ticket, rules, nearby):
    nearby = remove_invalid(rules, nearby)            
    valid_ind = {}
    known = {}
    for field, positions in rules.items():
        valid_ind[field] = []
        for ind in range(len(ticket)):
            min_0, max_0 = positions[0][0], positions[0][1]
            min_1, max_1 = positions[1][0], positions[1][1]
            f_func = lambda x: (min_0 <= x <= max_0) or (min_1 <= x <= max_1)
            if all(map(f_func, [n[ind] for n in nearby])):
                valid_ind[field].append(ind)
    while len(known) < len(valid_ind):
        for field, indices in valid_ind.items():
            if len(indices) == 1:
                known[field] = indices[0]
            else:
                for i in indices:
                    if i in known.values():
                        valid_ind[field].remove(i)
    
    result = 1
    for field, index in known.items():
        if "departure" in field:
            result *= ticket[index]
    return result

rules, ticket, nearby = read_inp("input")
print(part_two(ticket, rules, nearby))
