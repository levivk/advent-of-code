def p1():

    with open('day3_in.txt') as f:
        lines = f.readlines()

    binlen = len(lines[0].strip())
    
    count = [0] * binlen
    for l in lines:
        for i in range(binlen):
            if l[i] == '1':
                count[i] += 1

    th = len(lines) / 2
    gamma_str = ''.join('1' if c > th else '0' for c in count)
    ep_str = ''.join('1' if c=='0' else '0' for c in gamma_str)
    g = int(gamma_str, 2)
    e = int(ep_str, 2)
    print(count)
    print(g,e)
    print(gamma_str, ep_str)
    print(g*e)
    print(binlen)
    print(len(lines[0].strip()), lines[0])

p1()