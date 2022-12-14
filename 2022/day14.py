with open('day14_in.txt') as f:
    lines = f.readlines()

points = [[[int(x) for x in coord.split(',')] for coord in line.split(' -> ')] for line in lines]
rock_lines = []
rocks = set()
for l in points:
    rock_line = []
    for c1,c2 in zip(l[:-1], l[1:]):
        x1 = c1[0]
        x2 = c2[0]
        y1 = c1[1]
        y2 = c2[1]
        if x1 == x2:
            sign = int((y2 - y1) / abs(y2 - y1))
            new_rocks = [(x1, y) for y in range(y1, y2+sign, sign)]
        elif y1 == y2:
            sign = int((x2 - x1) / abs(x2 - x1))
            new_rocks = [(x, y1) for x in range(x1, x2+sign, sign)]
        else:
            raise Exception(f"Not a straight line? c1: {c1}, c2: {c2}")
        rock_line.append(new_rocks)
        rocks.update(new_rocks)
    rock_lines.append(rock_line)

# print(rock_lines[0])
# print(rocks)

def p1():

    max_y = max([c[1] for c in rocks])
    sand = set()
    done = False
    while(not done):
        # new sand
        x = 500
        for y in range(max_y+1):
            if y == max_y:
                done = True
                break
            elif (x,y+1) not in rocks and (x,y+1) not in sand:
                # Nothing below
                pass
            elif (x-1,y+1) not in rocks and (x-1,y+1) not in sand:
                # Nothing down left
                x -= 1
            elif (x+1,y+1) not in rocks and (x+1,y+1) not in sand:
                # Nothing down right
                x += 1
            else:
                # stop here
                sand.add((x,y))
                break

    print(len(sand))

# I originally tried checking in a union of rocks and sand, but it seems it must use new memory for
#       the union instead of just checking in both. Makes sense in retrospect. for sets of 250,000,
#       union takes 20 ms while below takes 35 ns
def p2():
    max_y = max([c[1] for c in rocks])
    floor = max_y + 2
    sand = set()
    done = False
    # i = 0
    while(not done):
        # new sand
        x = 500
        # print('*', end='')
        for y in range(floor + 1):
            if y+1 == floor:
                #stop
                sand.add((x,y))
                break
            elif (x,y+1) not in rocks and (x,y+1) not in sand:
                # Nothing below
                pass
            elif (x-1,y+1) not in rocks and (x-1,y+1) not in sand:
                # Nothing down left
                x -= 1
            elif (x+1,y+1) not in rocks and (x+1,y+1) not in sand:
                # Nothing down right
                x += 1
            else:
                # stop here
                sand.add((x,y))
                if (x,y) == (500,0):
                    done = True
                break
        # if i % 100 == 0:
        #     print(i)
        # i += 1
    print(len(sand))

# p1()
p2()