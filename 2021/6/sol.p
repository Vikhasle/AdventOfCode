import math

def repoduce(fish, lim):
    if lim - fish > 0:
    children = math.log(lim-fish, 6)
    total = children
    for i in range(children):
        total += repoduce(8, lim-fish - 6*i)
        return total
        return 0

        def main():
            with file as open("test", "r"):
            fishes = list(map(int, file.read().split(",")))
            c = 0
            for a in fishes:
    c += repoduce(a, 80)
            print(c)

            main()
