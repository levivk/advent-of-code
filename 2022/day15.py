import re
from tqdm import tqdm

with open('day15_in.txt') as f:
    lines = f.readlines()

sb = []
for l in lines:
    n = re.findall('-?[0-9]+', l)
    sb.append(((int(n[0]),int(n[1])),(int(n[2]),int(n[3]))))

def distance(a,b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

# compute distance from each sensor to beacon
sensor_dist = {s:distance(s,b) for s,b in sb}
# print(sensor_dist)

minx = min([s[0] - sensor_dist[s] for s,_ in sb])
maxx = max([s[0] + sensor_dist[s] for s,_ in sb])
beacons = set([b for _,b in sb])
sensors = set([s for s,_ in sb])
print(minx, maxx)

def p1():
    
    no_beacons = 0
    # expand range just in case I'm off
    for x in tqdm(range(minx-1,  maxx+2)):
        c = (x,2000000)
        # if this coord is same or closer to sensor than known beacon
        if any([distance(c,s) <= sensor_dist[s] for s,_ in sb]) and c not in beacons:
            no_beacons += 1

    print(no_beacons)

def p2():

    # if there is only one possible position, it will be bordered by the perimter
    # of a beacon distance. Search around the perimter of beacon distances.

    def in_range(c):
        if 0 <= c[0] <= 4000000 and 0 <= c[1] <= 4000000:
            return True
        else:
            return False

    def lr_of_perim(s):
        d = sensor_dist[s]
        x = s[0]
        y = s[1]
        # top to right
        for c in zip(range(x,x + (d+1)), range(y - (d+1),y)):
            if in_range(c): yield c
        # right to bottom
        for c in zip(range(x + (d+1), x, -1), range(y, y + (d+1))):
            if in_range(c): yield c
        # bottom to left
        for c in zip(range(x, x - (d+1), -1), range(y + (d+1), y, -1)):
            if in_range(c): yield c
        # left to top
        for c in zip(range(x - (d+1), x), range(y, y+(d+1), -1)):
            if in_range(c): yield c

    tried = 0
    for s,_ in sb:
        for c in lr_of_perim(s):
            if not any([distance(c,s) <= sensor_dist[s] for s,_ in sb]) and c not in beacons and c not in sensors:
                print(c)
                exit()
            else:
                tried += 1
            if tried % 100000 == 0:
                print(tried)

# p1()
p2()
