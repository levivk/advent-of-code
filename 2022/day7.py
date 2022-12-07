with open('day7_in.txt') as f:
    lines = f.readlines()

i = 0
curdir = '/'
sizes = {'/':0}
while i < len(lines):

    l = lines[i]
    if l[0] != '$':
        print("Not at $. Bad parsing")
        exit()

    if l[2:4] == 'cd':

        if l[5] == '/':
            curdir = '/'
        elif l[5:7] == '..':
            try:
                idx = curdir.rindex('/', 0, -1)
            except ValueError:
                print(curdir)
                exit()
            curdir = curdir[:idx+1]
        else:
            curdir = curdir + l[5:].strip() + '/'
            if curdir not in sizes:
                sizes[curdir] = 0

        i += 1

    elif l[2:4] == 'ls':
        i += 1
        l = lines[i]
        while(l[0] != '$'):

            if l[:3] == 'dir':
                pass
            else:
                idx = l.index(' ')
                s = int(l[:idx])
                sizes[curdir] += s

                # add to all other sizes
                cd2 = curdir
                while(cd2 != '/'):
                    idx = cd2.rindex('/', 0, -1)
                    cd2 = cd2[:idx+1]
                    sizes[cd2] += s

            i += 1
            if i == len(lines): break
            l = lines[i]

s = 0
for d in sizes:
    if sizes[d] < 100000:
        s += sizes[d]

print(s)

free = 70000000 - sizes['/']
need = 30000000 - free
print('size /:', sizes['/'])
print('need:', need)
si = list(sizes.values())
si.sort()

for i,n in enumerate(si):
    if n > need:
        print(n)
        break

# print(si)