import string
import networkx as nx

with open('day12_in.txt') as f:
    lines = f.readlines()

out = list(range(26))
l2n = dict(zip(string.ascii_lowercase, range(26)))
l2n['S'] = -1 
l2n['E'] = 26 
squares = [list(l.strip()) for l in lines]
squares = [[l2n[c] for c in s] for s in squares]

G = nx.DiGraph()
level_a = []
start = None
end = None

def can_move(a,b):
    if (a-b) >= -1:
        return True
    else:
        return False

for i in range(len(squares)):
    for j in range(len(squares[0])):

        t = squares[i][j]
        u = squares[i-1][j] if i > 0 else None
        d = squares[i+1][j] if i < len(squares) - 1 else None
        l = squares[i][j-1] if j > 0 else None
        r = squares[i][j+1] if j < len(squares[0]) -1 else None

        if t == -1:
            start = (i,j)
        elif t == 26:
            end = (i,j)

        if t == 0:
            level_a.append((i,j))

        if u != None and can_move(t,u):
            G.add_edge((i,j),(i-1,j))
        if d != None and can_move(t,d):
            G.add_edge((i,j),(i+1,j))
        if l != None and can_move(t,l):
            G.add_edge((i,j),(i,j-1))
        if r != None and can_move(t,r):
            G.add_edge((i,j),(i,j+1))

# print(G.edges())
# part a
path = nx.shortest_path(G, start, end)
# print(path)
# print(len(path)-1)

# part b
path_b = nx.shortest_path(G, target=end)
lengths = [len(path_b[a])-1 for a in level_a if a in path_b]
print(min(lengths))