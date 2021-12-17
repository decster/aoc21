import sys
from collections import defaultdict
from itertools import chain

ls = [e.strip() for e in sys.stdin.readlines()]

l = ls[0]

d = {}
for e in ls[2:]:
    fs = e.split(' -> ')
    d[fs[0]] = fs[1]

def step():
    global l
    nl = l[0]
    for i in range(1, len(l)):
        nl += d[l[i-1:i+1]]
        nl += l[i]
    l = nl
    #print(l)


for i in range(10):
    step()
    cnt = defaultdict(int)
    for c in l:
        cnt[c] += 1
    cnts = sorted(cnt.values())
    print(cnts)

print(cnts[-1] - cnts[0])
