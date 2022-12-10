import numpy as np

with open('day10_in.txt') as f:
    lines = f.readlines()

def p1():
    ss = 0
    cycle = 0
    x = 1

    def test_cycle(c, s, x):
        if c in [20,60,100,140,180,220]:
            s += c * x
            print(s,c,x)
        return s

    for l in lines:
        l.strip()
        inst = l[:4]

        if inst == 'noop':
            cycle += 1
            ss = test_cycle(cycle, ss, x)
        elif inst == 'addx':
            val = int(l[5:])
            cycle += 1
            ss = test_cycle(cycle, ss, x)
            cycle += 1
            ss = test_cycle(cycle, ss, x)
            x += val

    print(ss)

def p2():
    cycle = 0
    x = 1

    screen = [['-' for _ in range(6)] for _ in range(40)]
    print(len(screen), len(screen[0]))

    def test_cycle(cycle, x):

        h = (cycle -1)% 40
        v = int((cycle -1)// 40)
        print(h,v)

        if h in [x-1, x, x+1]:
            screen[h][v] = '#'
        else:
            screen[h][v] = '.'

    for l in lines:
        l.strip()
        inst = l[:4]

        if inst == 'noop':
            cycle += 1
            ss = test_cycle(cycle, x)
        elif inst == 'addx':
            val = int(l[5:])
            cycle += 1
            ss = test_cycle(cycle, x)
            cycle += 1
            ss = test_cycle(cycle, x)
            x += val

    # Transposed but oh well
    p = ""
    for s in screen:
        for c in s:
            p += c
        p += '\n'
    print(p)
p2()