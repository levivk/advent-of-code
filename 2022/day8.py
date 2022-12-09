import numpy as np

def p1():
    vis_idxs = set()
    def count_vis(a, xidx, yidx, reverse):
        m = -1
        for i,ai in enumerate(a):
            if ai > m:
                m = ai
                if not reverse:
                    if xidx != None:
                        idx=(xidx,i)
                    else:
                        idx=(i,yidx)
                else:
                    if xidx != None:
                        idx=(xidx,dim-i-1)
                    else:
                        idx=(dim-i-1,yidx)
                if idx not in vis_idxs:
                    vis_idxs.add(idx)
    count = 0
    for xi in range(dim):
        count_vis(grid[xi], xidx=xi, yidx=None, reverse=False)
        count_vis(grid[xi,::-1], xidx=xi, yidx=None, reverse=True)
    for yi in range(dim):
        count_vis(grid[:,yi], xidx=None, yidx=yi, reverse=False)
        count_vis(grid[::-1,yi], xidx=None, yidx=yi, reverse=True)

    print(len(vis_idxs))

def p2():

    def look(ar,height):
        c = 0
        for ai in ar:
            if ai < height:
                c+=1
            else:
                c+=1
                break
        return c


    score = np.ones((dim,dim))
    for idx,h in np.ndenumerate(grid):
        x = idx[0]
        y = idx[1]
        score[idx] *= look(grid[x+1:,y], h)
        score[idx] *= look(np.flip(grid[:x, y]), h)
        score[idx] *= look(grid[x,y+1:], h)
        score[idx] *= look(np.flip(grid[x,:y]), h)

    print(np.unravel_index(np.argmax(score), score.shape))
    # np.set_printoptions(threshold=np.inf)
    print(np.max(score))


with open('day8_in.txt') as f:
    lines = f.readlines()

dim = len(lines)
grid = np.zeros((dim,dim))
for i,l in enumerate(lines):
    grid[i] = [int(li) for li in l.strip()]

p1()
# p2()
# print(vis_idxs)