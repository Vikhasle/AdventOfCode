def gamma(pos, b_strs):
    counter = 0
    for bstr in b_strs:
        if bstr[pos] == '1':
            counter +=1
        else: counter -=1
    return '1' if counter >= 0 else '0'

def eps(pos, b_strs):
    counter = 0
    for bstr in b_strs:
        if bstr[pos] == '1':
            counter +=1
        else: counter -=1
    return '0' if counter >= 0 else '1'

def btoi(b_str):
    res = 0
    for char in b_str:
        res <<= 1
        if char == '1':
            res +=1
    return res

def part_two():
    valid = [x.strip() for x in strings]
    valid2 = list(valid)
    c = 0
    while len(valid) > 1:
        g = gamma(c, valid)
        valid = list(filter(lambda x : x[c] == g, valid))
        c+=1
    c = 0
    while len(valid2) > 1:
        g = eps(c, valid2)
        valid2 = list(filter(lambda x : x[c] == g, valid2))
        c+=1
    print(valid, valid2)
    print(btoi(valid[0])*btoi(valid2[0]))

strings = open("input", "r").readlines()
part_two()
