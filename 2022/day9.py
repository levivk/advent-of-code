# With help from chatgpt which ended up not being worth it
import numpy as np

with open('day9_in.txt') as f:
    series = f.readlines()


# Define the possible movements for the head
movements = {
    "U": np.array([0,-1]),
    "D": np.array([0, 1]),
    "L": np.array([-1,0]),
    "R": np.array([1, 0])
}


def tail_from_head(head, tail):
    dif = head - tail
    if np.all(np.abs(dif) <= 1):
        # if tail is adjacent do not move
        pass
    else:
        tail += np.clip(dif, -1, 1)

    return tail

def p1():

    # Define the starting position of the head and tail
    head = np.zeros(2)
    tail = np.zeros(2)

    pos = []
    pos.append(tuple(tail))

    # Iterate over the series of movements
    for movement in series:
        # Parse the movement and its distance
        direction, distance = movement.split()
        distance = int(distance)
        
        for _ in range(distance):
            dx = movements[direction]
            head += dx
            tail = tail_from_head(head, tail)
            pos.append(tuple(tail))

    print(len(set(pos)))
    

def p2():

    knots = [np.zeros(2) for _ in range(10)]
    pos = []
    pos.append(tuple(knots[-1]))

    for m in series:
        dirc, dist = m.split()
        dist = int(dist)

        for _ in range(dist):
            dx = movements[dirc]
            knots[0] = knots[0] + dx
            for i in range(len(knots)-1):
                k1 = knots[i]
                k2 = knots[i+1]
                knots[i+1] = tail_from_head(k1,k2)
            pos.append(tuple(knots[-1]))

    print(len(set(pos)))


p2()