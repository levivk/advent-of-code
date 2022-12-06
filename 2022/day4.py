def p1():
    s = 0
    for l in lines:
        l = l.strip()
        s1,s2 = l.split(',')
        e11,e12 = s1.split('-')
        e21,e22 = s2.split('-')
        set1 = set(range(int(e11), int(e12)+1))
        set2 = set(range(int(e21), int(e22)+1))
        if set1 <= set2 or set2 <= set1:
            s += 1
    print(s)

def p2():
    s = 0
    for l in lines:
        l = l.strip()
        s1,s2 = l.split(',')
        e11,e12 = s1.split('-')
        e21,e22 = s2.split('-')
        set1 = set(range(int(e11), int(e12)+1))
        set2 = set(range(int(e21), int(e22)+1))
        if len(set1 & set2) != 0:
            s += 1

    print(s)


with open('day4_in.txt') as f:
    lines = f.readlines()

p1()
p2()
