import re
import networkx as nx

with open('day16_in.txt') as f:
    lines = f.readlines()

flow_rate = {}
G = nx.DiGraph()
for l in lines:
    valves = re.findall('[A-Z]{2}', l)
    # print(valves)
    v = valves[0]
    G.add_weighted_edges_from([(v,v2,1) for v2 in valves[1:]])
    rate = re.findall('[0-9]+', l)
    rate = int(rate[0])
    flow_rate[v] = rate

# print(G.nodes())


# remove nodes with flow rate 0
for n1 in list(G):
    if flow_rate[n1] == 0:
        for n0 in G.predecessors(n1):
            w1 = G.edges[(n0,n1)]['weight']
            for n2 in G.successors(n1):
                w2 = G.edges[(n1,n2)]['weight']
                if n0 != n2 and (n0,n2) not in G.edges():
                    G.add_edge(n0, n2, weight=w1+w2)
        if n1 != 'AA':
            G.remove_node(n1)
        else:
            # remove all edges into AA
            for n0 in list(G.predecessors(n1)):
                G.remove_edge(n0,n1)

flow_rate = {n:flow_rate[n] for n in G}

# for a,b in flow_rate.items():
#     print(a,b)
# add edges to skip over


# print(G.nodes())

# for n1,n2,w in G.edges.data('weight', default=0):
#     print(n1,n2,w)



def p1():

    maxp = 0
    n_paths = 0

    def step(valve, minute, cump, openv, ppm):

        def test_time(m, cump):
            nonlocal maxp
            nonlocal n_paths
            if m >= 31:
                if cump > maxp:
                    maxp = cump
                n_paths += 1
                if(n_paths % 10 == 0): print(n_paths)
                return True
            else:
                return False

        # we are at valve, we want to try moving to adjacent valves both with opening this valve and not
        # Do not revisit we can also try staying here till the end

        # with opening
        if flow_rate[valve] != 0 and valve not in openv:
            minute2 = minute
            cump2 = cump
            ppm2 = ppm

            cump2 += ppm2
            # openv.append(valve)
            ppm2 += flow_rate[valve]
            minute2 += 1
            if test_time(minute2, cump): return

            for n in G.successors(valve):
                w = G.edges[(valve,n)]['weight']
                minute2 += w
                if test_time(minute2, cump): return
                step(n, minute2, cump2 + (ppm2*w), openv + [valve], ppm2)

        # without opening
        for n in G.successors(valve):
            w = G.edges[(valve,n)]['weight']
            minute += w
            if test_time(minute, cump): return
            step(n, minute, cump+(w*ppm), openv, ppm)

        return

    m = 1
    v = 'AA'
    cump = 0
    openv = []
    ppm = 0
    step(v, m, cump, openv, ppm)
    print(maxp)

p1()