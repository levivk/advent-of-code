import numpy as np

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


area = 0
for c in cubes:
    nc = 6
    for s in sides(c):
        if s in cubes:
            nc -= 1
    area += nc

print(area)
    