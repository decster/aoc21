import sys
from collections import defaultdict
from itertools import chain

ls = [e.strip().split('-') for e in sys.stdin.readlines()]

all = set()

def dfs(g, n, p, m):
    for d in g[n]:
        #print(f'dfs {n} -> {d}  {p}')
        if d == 'end':
            all.add(','.join(p))
            continue
        U = d[0].isupper()
        if U or (d not in m):
            if not U:
                m.add(d)
            p.append(d)
            dfs(g, d, p, m)
            p.pop()
            if not U:
                m.remove(d)

def main():
    g = defaultdict(list)
    for e in ls:
        if e[0] != 'end' and e[1] != 'start':
            g[e[0]].append(e[1])
        if e[0] != 'start' and e[1] != 'end':
            g[e[1]].append(e[0])
    # for n, ds in g.items():
    #     for d in ds:
    #         print(f'{n} -> {d}')
    dfs(g, 'start', [], set())
    for e in all:
        print(e)
    print(len(all))

main()
