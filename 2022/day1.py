def p1():

    with open('day1_in.txt') as f:
        lines = f.readlines()

    s = 0
    m = 0
    for l in lines:

        if l.strip() == '':
            if s > m:
                m = s
            s = 0

        else:
            s += int(l)

    print(m)

def p2():

    with open('day1_in.txt') as f:
        lines = f.readlines()

    s = 0
    m = []
    for l in lines:

        if l.strip() == '':
            m.append(s)
            s = 0

        else:
            s += int(l)

    m.sort()
    print(sum(m[-3:]))


p1()
p2()