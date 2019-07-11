d = ['' for _ in range(10)]
d[0] = ["+---+", "|   |", "|   |", "+   +", "|   |", "|   |", "+---+"]
d[1] = ["    +", "    |", "    |", "    +", "    |", "    |", "    +"]
d[2] = ["+---+", "    |", "    |", "+---+", "|    ", "|    ", "+---+"]
d[3] = ["+---+", "    |", "    |", "+---+", "    |", "    |", "+---+"]
d[4] = ["+   +", "|   |", "|   |", "+---+", "    |", "    |", "    +"]
d[5] = ["+---+", "|    ", "|    ", "+---+", "    |", "    |", "+---+"]
d[6] = ["+---+", "|    ", "|    ", "+---+", "|   |", "|   |", "+---+"]
d[7] = ["+---+", "    |", "    |", "    +", "    |", "    |", "    +"]
d[8] = ["+---+", "|   |", "|   |", "+---+", "|   |", "|   |", "+---+"]
d[9] = ["+---+", "|   |", "|   |", "+---+", "    |", "    |", "+---+"]

while True:
    s = input()
    if s == 'end':
        print('end')
        break

    for y in range(7):
        o = ''
        for c in s:
            if c == ':':
                if y == 2 or y == 4:
                    o += 'o'
                else:
                    o += ' '
            else:
                c = int(c)
                for x in range(5):
                    o += d[c][y][x]
            o += '  '
        print(o[:-2])
    print()
    print()