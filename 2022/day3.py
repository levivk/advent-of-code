import string

let_to_p = dict(zip(string.ascii_letters, range(1,53)))


def p1():

    with open('day3_in.txt') as f:
        lines = f.readlines()

    s = 0
    for l in lines:
        l = l.strip()

        r1 = l[:int(len(l)/2)]
        r2 = l[int(len(l)/2):]

        same = ''
        for r in r1:
            if r in r2:
                same = r
                break

        
        print(same, let_to_p[same])
        s += let_to_p[same]
    print(s)


def p2():
    with open('day3_in.txt') as f:
        lines = f.readlines()

    s = 0
    for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
        # print(l1[0], l2[0], l3[0])
        same = ''
        for r in l1:
            if r in l2 and r in l3:
                same = r
                break

        s += let_to_p[same]
    print(s)


p1()
p2()