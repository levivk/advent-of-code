
def p1():

    with open('day2_in.txt') as f:
        lines = f.readlines()

    s = 0
    for l in lines:
        s2 = 0
        a,b = l.strip().split(' ')

        print(a,b)
        c = 'ABC'.index(a)
        d = 'XYZ'.index(b)

        s2 += d+1

        if c == d:
            s2 += 3
        elif c  == 2 and d == 0:
            s2 += 6
        elif c == 0 and d == 2:
            pass
        elif c < d:
            s2 += 6

        print(s2)
        s += s2

    print(s)

def p2():

    with open('day2_in.txt') as f:
        lines = f.readlines()

    s = 0
    for l in lines:
        s2 = 0
        a,b = l.strip().split(' ')

        score = {
            'A X': 3,
            'B X': 1,
            'C X': 2,
            'A Y': 1,
            'B Y': 2,
            'C Y': 3,
            'A Z': 2,
            'B Z': 3,
            'C Z': 1,
            }

        print(a,b)
        c = 'ABC'.index(a)
        d = 'XYZ'.index(b)

        # score for what played
        s2 += score[l.strip()]

        # winning score
        s2 += d*3


        print(s2)
        s += s2

    print(s)

p1()
p2()