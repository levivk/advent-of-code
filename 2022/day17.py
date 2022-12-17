import numpy as np

with open('day17_in.txt') as f:
    gas = f.read().strip()

rocks = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,0), (0,1), (1,1), (2,1), (1,2)],
    [(0,0), (1,0), (2,0), (2,1), (2,2)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (0,1), (1,0), (1,1)]
]

gd = {'<':np.array([-1,0]), '>':np.array([1,0])}
down = np.array([0,-1])

def max_height(arr):
    try:
        return np.where(arr.any(axis=0))[0].max()
    except ValueError:
        # floor is at -1
        return -1

def p1():
    fallen = np.zeros((7,8000), dtype=bool)
    gidx = 0
    for i in range(2022):
        ri = i % len(rocks)
        r = np.array(rocks[ri])

        rx = 2
        ry = max_height(fallen) + 4

        r += np.array([rx,ry])

        while(True):

            # move left right
            d = gas[gidx]
            gidx = (gidx + 1) % len(gas)
            r += gd[d]
            # revert if x < 0 or x >6 or collision
            if (r[:,0] < 0).any() or (r[:,0] > 6).any() or fallen[r[:,0], r[:,1]].any():
                r -= gd[d]

            # move down
            r += down

            # Check for collision: y < 0 or any points in fallen
            if (r[:,1] < 0).any() or fallen[r[:,0], r[:,1]].any():
                r -= down
                fallen[r[:,0], r[:,1]] = True
                break
    print(max_height(fallen)+1)

def p2():
    # find where start of rock cycle and start of gas direction cycle line up
    fallen = np.zeros((7,800000), dtype=bool)
    gidx = 0

    # first number is rocks before first pattern loop, second is rocks after last pattern loop
    for i in range(1757 + 1403):
        ri = i % len(rocks)
        r = np.array(rocks[ri])

        # if not first and ri == 0 and gidx % len(gas) == 0:
        #     print(f'rocks: {i}, height: {max_height(fallen)}')
        #     break
        # first = False

        rx = 2
        ry = max_height(fallen) + 4

        r += np.array([rx,ry])

        shift = 0
        while(True):
            if gidx == 0:
                print(f'rock: {ri}, rocks: {i}, shift: {shift}, height: {max_height(fallen)+1}')

            # move left right
            d = gas[gidx]
            gidx = (gidx + 1) % len(gas)
            r += gd[d]
            # revert if x < 0 or x >6 or collision
            if (r[:,0] < 0).any() or (r[:,0] > 6).any() or fallen[r[:,0], r[:,1]].any():
                r -= gd[d]

            # move down
            r += down

            # Check for collision: y < 0 or any points in fallen
            if (r[:,1] < 0).any() or fallen[r[:,0], r[:,1]].any():
                r -= down
                fallen[r[:,0], r[:,1]] = True
                break
            shift += 1
    # height of 1757+1403 rocks + num patterns * height per pattern
    print((max_height(fallen)+1) + (1000000000000-1757-1403) // 1755 * 2747)

p2()


