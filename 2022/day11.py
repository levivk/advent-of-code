# with open('day10_in.txt') as f:
#     data = f.read().split('\n\n')
#     monkey_lines = [m.split('\n') for m in data.split('\n\n')]

from tqdm import tqdm

class monkey():

    def __init__(self, i, o, t):
        self.items = i
        # takes old worry, returns new
        self.operation = o
        # takes worry, returns monkey
        self.test = t
        self.thrown_to = []
        self.inspected = 0
        

m0 = monkey(
    [59,74,65,86], 
    lambda w : w*19, 
    lambda w : 6 if (w % 7 == 0) else 2
)
m1 = monkey(
    [62, 84, 72, 91, 68, 78, 51],
    lambda w : w+1,
    lambda w : 2 if (w % 2 == 0) else 0
)
m2 = monkey(
    [78, 84, 96],
    lambda w : w + 8,
    lambda w : 6 if (w % 19 == 0) else 5
)
m3 = monkey(
    [97, 86],
    lambda w : w*w,
    lambda w : 1 if (w % 3 == 0) else 0
)
m4 = monkey(
    [50],
    lambda w : w+6,
    lambda w : 3 if (w % 13 == 0) else 1
)
m5 = monkey(
    [73, 65, 69, 65, 51],
    lambda w : w*17,
    lambda w : 4 if (w % 11 == 0) else 7
)
m6 = monkey(
    [69, 82, 97, 93, 82, 84, 58, 63],
    lambda w : w+5,
    lambda w : 5 if (w % 5 == 0) else 7
)
m7 = monkey(
    [81, 78, 82, 76, 79, 80],
    lambda w : w+3,
    lambda w : 3 if (w % 17 == 0) else 4
)
monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]

def p1():
    # round loop
    for r in range(20):
        # each monkey takes a turn
        for m in monkeys:
            # monkey operates on each item
            for i in m.items:
                # worry level changes as monkey inspects
                new = m.operation(i)
                new = int(new / 3)
                next_monkey = m.test(new)
                m.thrown_to.append(next_monkey)
                monkeys[next_monkey].items.append(new)
                m.inspected += 1
            m.items = []

    insp = [m.inspected for m in monkeys]
    insp.sort(reverse=True)
    for i,m in enumerate(monkeys):
        print(f"monkey {i} threw to {m.thrown_to}")
    print("monkey business:", insp[0] * insp[1])

def p2():
    wrap = 7*2*19*3*13*11*5*17
    # round loop
    for r in tqdm(range(10000), disable=False):
        # each monkey takes a turn
        if r == 30:
            print(max([max(m.items) for m in monkeys if m.items != []]))
        for m in monkeys:
            # monkey operates on each item
            for i in m.items:
                # worry level changes as monkey inspects
                new = m.operation(i)
                # new = int(new / 3)
                new = new % wrap
                next_monkey = m.test(new)
                monkeys[next_monkey].items.append(new)
                m.inspected += 1
            m.items = []

    insp = [m.inspected for m in monkeys]
    insp.sort(reverse=True)
    print("monkey business:", insp[0] * insp[1])

p2()