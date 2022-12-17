import re
import networkx as nx
import itertools as it

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
for n1 in set(G):
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
valves = set(G) - set('AA')


# # add node for activating valve
# for n1 in set(G) - set('AA'):
#     n15 = n1 + "'"
#     G.add_edge(n1,n15, weight=1)
#     for n2 in G.successors(n1):
#         w = G.edges[(n1,n2)]['weight']
#         G.add_edge(n15,n2, weight = w)


# find all simple paths
# paths = []
# for n2 in G:
#     paths.extend(nx.all_simple_paths(G, 'AA', n2))

# for p in paths.copy():
#     if nx.path_weight(G,p,'weight') 


# calculate the released pressure

# def calc_released_pressure(path):
#     zzz
# print(len(paths))

# for a,b in flow_rate.items():
#     print(a,b)
# add edges to skip over


# print(G.nodes())

for n1,n2,w in G.edges.data('weight', default=0):
    print(n1,n2,w)



def p1():
    # assumption made: If you go past a valve, you take a minute to open it. This assumption is not true for the example, but is true for my input.

    maxp = 0
    n_paths = 0
    valve_order = []
    best_hist = []

    def step(valve, time, cum_p, openv, ppm, history):

        def test(cum_p, openv):
            nonlocal maxp
            nonlocal n_paths
            nonlocal valve_order
            nonlocal best_hist
            if cum_p > maxp:
                maxp = cum_p
                valve_order = openv
                best_hist = history
            n_paths += 1
            if(n_paths % 10 == 0): print(n_paths)

        # open valve and go to any unopened neighbors
        for n in G.successors(valve):
            if n in openv:
                test(cum_p + (ppm*time), openv)
                continue
            w = G.edges[(valve,n)]['weight']
            time_left = time - w - 1
            if time_left <= 0:
                test(cum_p + (ppm*time), openv)
                continue
            # if test_time(time_left, cum_p): continue
            step(n, time_left, cum_p + (ppm*(w+1)), openv + [n], ppm + flow_rate[n], history + [(n,ppm) for _ in range(w+1)])

    m = 30
    v = 'AA'
    cum_p = 0
    openv = []
    ppm = 0
    step(v, m, cum_p, openv, ppm, [('AA',0)])
    print(maxp, valve_order)
    print(best_hist)

def p2():

    # assumption made: If you go past a valve, you take a minute to open it. This assumption is not true for the example, but is true for my input.

    maxp = 0
    n_paths = 0
    valve_order = []
    best_hist = []

    def step(valve, time, cum_p, openv, ppm, history):

        def test(cum_p, openv):
            nonlocal maxp
            nonlocal n_paths
            nonlocal valve_order
            nonlocal best_hist
            if cum_p > maxp:
                maxp = cum_p
                valve_order = openv
                best_hist = history
            n_paths += 1
            if(n_paths % 1000000 == 0): print(n_paths)

        # open valve and go to any unopened neighbors
        for n in G.successors(valve):
            if n in openv:
                test(cum_p + (ppm*time), openv)
                continue
            w = G.edges[(valve,n)]['weight']
            time_left = time - w - 1
            if time_left <= 0:
                test(cum_p + (ppm*time), openv)
                continue
            # if test_time(time_left, cum_p): continue
            step(n, time_left, cum_p + (ppm*(w+1)), openv + [n], ppm + flow_rate[n], history + [(n,ppm) for _ in range(w+1)])

    # Same as p1 but try all combos of elephant vs elf opening valves
    combinations = []
    for i in range(len(valves)):
        combinations.extend([set(c) for c in it.combinations(valves, i)])

    m = 0
    for c1 in combinations:
        step('AA', 26, 0, list(c1), 0, [])
        p1 = maxp
        maxp = 0
        c2 = valves - c1
        step('AA', 26, 0, list(c2), 0, [])
        p2 = maxp
        maxp = 0
        m = max(m, p1+p2)

    print(m)

p2()