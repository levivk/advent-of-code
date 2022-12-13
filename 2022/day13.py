import ast
from functools import cmp_to_key

RIGHT = -1
WRONG = 1
SAME = 0

with open('day13_in.txt') as f:
    pairs = f.read().split('\n\n')

pairs = [p.split() for p in pairs]
pairs = [[ast.literal_eval(pi) for pi in p] for p in pairs]

def compare(a,b):
    if type(a) != type(b):
        if type(a) != list: a = [a]
        elif type(b) != list: b = [b]

    if type(a) == list:
        for ai,bi in zip(a,b):
            result = compare(ai, bi)
            if result != SAME:
                return result

        # Check len
        if len(a) > len(b):
            return WRONG
        elif len(a) == len(b):
            return SAME
        else:
            return RIGHT
    elif type(a) == int:
        if a > b:
            return WRONG
        elif a == b:
            return SAME
        else:
            return RIGHT
    else:
        raise Exception("something bad")

def p1():
    s = 0
    for i,p in enumerate(pairs):
        p1,p2 = p
        # print(i, len(p1), len(p2))
        result = compare(p1,p2)
        if result == RIGHT:
            s += i+1
        # print(i, result)
    print(s)

def p2():
    packets = [pack for pair in pairs for pack in pair]
    packets.append([[2]])
    packets.append([[6]])
    # print(len(packets), len(pairs))
    packets.sort(key=cmp_to_key(compare))
    # print(packets)
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))

p1()
p2()