def input():
    f = open("AdventOfCode/input3.txt", "r").readlines()
    p = []
    for a in f:
        p.append(a[:-1])
    return p


from collections import defaultdict
import re

data = input()
claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
m = defaultdict(list)
overlaps = {}
for (claim_number, start_x, start_y, width, height) in claims:
  overlaps[claim_number] = set()
  for i in xrange(start_x, start_x + width):
    for j in xrange(start_y, start_y + height):
      if m[(i,j)]:
        for number in m[(i, j)]:
          overlaps[number].add(claim_number)
          overlaps[claim_number].add(number)
      m[(i,j)].append(claim_number)

print "a", len([k for k in m if len(m[k]) > 1])
print "b", [k for k in overlaps if len(overlaps[k]) == 0][0]
"""
def Partone(test):
    area = 0
    taken = []
    taken2 = []
    for inp in test:
        pos = inp[inp.find("@")+2:inp.find(":")]
        inp_area = inp[inp.find(":")+1:]
        for iy in range(0, int(inp_area[inp_area.find("x")+1:])):
            for ix in range(0, int(inp_area[:inp_area.find("x")])):
                valy = str(int(pos[pos.find(",")+1:])+iy)
                valx = str(int(pos[:pos.find(",")])+ix)
                if valx + "," + valy in taken:
                    area += 1
                    taken.remove(valx + "," + valy)
                    taken2.append(valx + "," + valy)
                    pass
                if valx+"," + valy not in taken2:
                    taken.append(valx+"," + valy)
        print(inp)
    print(area)
    return area


def Parttwo(test):
    claims = []
    for claim in test:
        pos = inp[inp.find("@")+2:inp.find(":")]
        inp_area = inp[inp.find(":")+1:]
        indenty =


Parttwo(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4]", "#3 @ 5,5: 2x2"])
"""
