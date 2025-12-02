def read_inp():
    fil = open("input", "r").read().split("\n")
    e = int(fil[0])
    buses = [x for x in fil[1].split(",")]
    for i in range(len(buses)):
        if buses[i] != 'x':
            buses[i] = int(buses[i])
    return e, buses


def part_one(earliest, ids):
    wait_times = {}
    for bus in ids:
        if bus == 'x':
            continue
        a = 0
        while (a + earliest) % int(bus) != 0:
            a += 1
        wait_times[int(bus)] = a
    mid, mw = 0, 999999999999
    for key in wait_times:
        if wait_times[key] < mw:
            mw = wait_times[key]
            mid = key
    return mw*mid


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part_two(buses):
    # Chinese Remainder theorem
    N = 1
    for bus in buses:
        if bus == 'x':
            continue
        N *= bus
    t = 0
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        y = N//bus
        t += (-1*i) * mul_inv(y, bus)*y
    return t % N

    # Bruteforce
    """
  roof = 1
  for bus in buses:
      if bus == 'x':
          continue
      roof *= int(bus)
  t = roof


  while True:
      found = True
      t -= int(buses[0])
      for i, bus in enumerate(buses):
          if bus == 'x':
              continue
          if (t+i) % int(bus) != 0:
              found = False
              break
      if found:
          return t"""


a, b = read_inp()
test = [7, 13, 'x', 'x', 59, 'x', 31, 19]
print(part_one(a, b))
print(part_two(b))
