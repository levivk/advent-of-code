

def p1():
    with open('day1_input.txt') as f:
        lines = f.readlines()

    count = 0
    count2 = 0
    for l1, l2 in zip(lines[:-1], lines[1:]):
        if int(l2) > int(l1):
            count += 1
        else:
            count2 += 1

    print(count, count2)

def p2():
    with open('day1_input.txt') as f:
        lines = f.readlines()

    lines_int = [int(l) for l in lines]
    count = 0
    for i in range(len(lines) - 3):
        s1 = sum(lines_int[i:i+3])
        s2 = sum(lines_int[i+1:i+4])
        if s2 > s1:
            count +=1 

    print(count)

if __name__ == '__main__':
    p2()