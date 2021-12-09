import sys
from collections import defaultdict
from itertools import chain

ls = sys.stdin.readlines()
dps = [l.split(' | ') for l in ls]
ds = [[frozenset(e) for e in s[0].split()] for s in dps]
ps = [[frozenset(e) for e in s[1].split()] for s in dps]


def solve(d, p):
    m = {}
    s1 = None
    d5 = set() # 2 3 5
    d6 = set() # 0 6 9
    for e in d:
        if len(e) == 2:
            m[e] = 1
            s1 = e
        elif len(e) == 3:
            m[e] = 7
        elif len(e) == 4:
            m[e] = 4
        elif len(e) == 7:
            m[e] = 8
        elif len(e) == 5:
            d5.add(e)
        elif len(e) == 6:
            d6.add(e)
    w3 = next(filter(lambda x: len(frozenset.intersection(s1,x)) == 2, d5))
    m[w3] = 3
    d5.remove(w3)
    w6 = next(filter(lambda x: len(frozenset.intersection(s1,x)) == 1, d6))
    m[w6] = 6
    d6.remove(w6)
    by_seg = defaultdict(int)
    for w in chain(d5,d6): # 2 5 0 9
        for c in w:
            by_seg[c]+=1
    sege = next(filter(lambda e: e[1]==2, by_seg.items()))[0]
    for w2_or_w5 in d5:
        if sege in w2_or_w5:
            m[w2_or_w5] = 2
        else:
            m[w2_or_w5] = 5
    for w0_or_w9 in d6:
        if sege in w0_or_w9:
            m[w0_or_w9] = 0
        else:
            m[w0_or_w9] = 9
    return sum(m[e] * (10**(3-i)) for i,e in enumerate(p))


def main():
    print(sum(solve(d,p) for d, p in zip(ds, ps)))

main()
