import numpy as np
from collections import deque

with open('day18_in.txt') as f:
    lines = f.readlines()

cubes = set()
for l in lines:
    l.strip()
    cubes.add(tuple([int(i) for i in l.split(',')]))

# sides = [
#     (-1,0,0),
#     (1,0,0),
#     (0,-1,0),
#     (0,1,0),
#     (0,0,-1),
#     (0,0,1)
# ]
# sides = [np.array(s) for s in sides]

def sides(c):
    yield (c[0]-1,c[1],c[2])
    yield (c[0]+1,c[1],c[2])
    yield (c[0],c[1]-1,c[2])
    yield (c[0],c[1]+1,c[2])
    yield (c[0],c[1],c[2]-1)
    yield (c[0],c[1],c[2]+1)

def p1():
    area = 0
    for c in cubes:
        nc = 6
        for s in sides(c):
            if s in cubes:
                nc -= 1
        area += nc

    print(area)
    return area
    
def p2():

    # create set of outside air starting with air on border. Find all neighboring airs. Others must be pockets
    air_low = min([x for c in cubes for x in c]) -1
    air_high = max([x for x in cubes for x in x]) +1
    print(air_low,air_high)

    def in_bounds(c):
        for x in c:
            if x < air_low or x > air_high:
                return False
        return True

    r = range(air_low, air_high+1)
    #outside air
    air = set([(a,b,air_low) for a in r for b in r])
    air.update([(a,b,air_high) for a in r for b in r])
    air.update([(a,air_low,b) for a in r for b in r])
    air.update([(a,air_high,b) for a in r for b in r])
    air.update([(air_low,a,b) for a in r for b in r])
    air.update([(air_high,a,b) for a in r for b in r])
    print('boundary air:', len(air))

    q = deque(air)

    # all outside air
    while len(q) != 0:
        c = q.popleft()
        for s in sides(c):
            if s in cubes or s in air or not in_bounds(s):
                continue
            air.add(s)
            q.append(s)
    print('total outside air:', len(air))

    # total cubes
    total = set([(a,b,c) for a in r for b in r for c in r])
    print('total cubes:', len(total))

    pockets = total - air - cubes
    print('air pockets:', len(pockets))

    # surface area of air pockets
    parea = 0
    for p in pockets:
        nc = 6
        for s in sides(p):
            if s in pockets:
                nc -= 1
            if s in air:
                raise Exception("Something wrong. Pocket next to air means it's not a pocket.")
        parea += nc
    print('pocket surface area:', parea)

    sarea = p1()
    real_area = sarea - parea
    print('outside surface area:', real_area)

p2()