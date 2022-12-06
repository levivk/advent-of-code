
def p1():
    for i, four_chars in enumerate(zip(l[::], l[1::], l[2::], l[3::])):
        if len(four_chars) == len(set(four_chars)):
            print(four_chars)
            print(i+4)
            break

def p2():
    slices = [l[j::] for j in range(14)]
    for i, four_chars in enumerate(zip(*slices)):
        if len(four_chars) == len(set(four_chars)):
            print(four_chars)
            print(i+14)
            break



with open('day6_in.txt') as f:
    lines = f.readlines()

l = lines[0]

p1()
p2()