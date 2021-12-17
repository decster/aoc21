import sys
from collections import defaultdict
from itertools import chain

ls = [e.strip().split('-') for e in sys.stdin.readlines()]

all = set()
sp = None

def dfs(g, n, p, m):
    global sp
    for d in g[n]:
        if d == 'end':
            all.add(','.join(p))
            continue
        NM = d not in m
        DSP = d == sp
        if d[0].isupper() or NM or DSP:
            if NM:
                m.add(d)
            elif DSP:
                sp = sp + '0'
            p.append(d)
            dfs(g, d, p, m)
            p.pop()
            if NM:
                m.remove(d)
            elif DSP:
                sp = sp[:-1]

def main():
    g = defaultdict(list)
    for e in ls:
        if e[0] != 'end' and e[1] != 'start':
            g[e[0]].append(e[1])
        if e[0] != 'start' and e[1] != 'end':
            g[e[1]].append(e[0])
    sps = list(filter(lambda x: x not in ('start', 'end') and x[0].islower(), g.keys()))
    # for n, ds in g.items():
    #     for d in ds:
    #         print(f'{n} -> {d}')
    dfs(g, 'start', [], set())
    global sp
    for e in sps:
        sp = e
        dfs(g, 'start', [], set())
    for e in all:
        print(e)
    print(len(all))

main()
