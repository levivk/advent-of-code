def p1():

    with open('day2_in.txt') as f:
        lines = f.readlines()

    h = 0
    d = 0

    for l in lines:
        c,w = l.split(' ')
        if c == 'forward':
            h += int(w)
        elif c == 'up':
            d -= int(w)
        elif c == 'down':
            d += int(w)
        else:
            print('help')

    print(h*d)
        

def p2():

    with open('day2_in.txt') as f:
        lines = f.readlines()

    h = 0
    d = 0
    a = 0

    for l in lines:
        c,w = l.split(' ')
        w = int(w)
        if c == 'forward':
            h += w
            d += a * w
        elif c == 'up':
            a -= w
        elif c == 'down':
            a += w
        else:
            print('help')

    print(h*d)


if __name__ == '__main__':
    p2()