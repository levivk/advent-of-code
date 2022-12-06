import string
import re

# def move_crate(num, st1, st2)

def p1():
    for l in lines[10:]:
        move,a,b = re.findall(r'\d+', l)
        a = int(a) - 1
        b = int(b) - 1
        for _ in range(int(move)):
            foo = stacks[a].pop()
            stacks[b].append(foo)

    print([s[-1] for s in stacks])


def p2():

    for l in lines[10:]:
        move,a,b = re.findall(r'\d+', l)
        a = int(a) - 1
        b = int(b) - 1
        move = int(move)
        foo = stacks[a][-move:]
        stacks[a] = stacks[a][:-move]
        stacks[b].extend(foo)

    print([s[-1] for s in stacks])


with open('day5_in.txt') as f:
    lines = f.readlines()

stacks = [[] for _ in range(9)]
i = 0
l = lines[i]
while(l != '\n'):
    # l = l.replace('[', '')
    # l = l.replace(']', '')
    # crates = l.split(' ')
    for j,c in enumerate(l):
        if c in string.ascii_uppercase:
            idx = int((j-1)/4)
            print(idx, c)
            stacks[idx].insert(0,c)

    i += 1
    l = lines[i]
print(stacks[0])

# stacks = [
#     ['R']
# ]

# p1()
p2()
