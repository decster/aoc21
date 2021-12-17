import sys
from collections import defaultdict
from itertools import chain

ls = [e.strip() for e in sys.stdin.readlines()]

l = ls[0]
ld = defaultdict(int)
for i in range(len(l)-1):
    ld[l[i:i+2]]+=1

d = {}
for e in ls[2:]:
    fs = e.split(' -> ')
    d[fs[0]] = (fs[0][0]+fs[1], fs[1]+fs[0][1])

def step():
    global ld
    nld = defaultdict(int)
    for k,v in ld.items():
        a, b = d[k]
        nld[a]+=v
        nld[b]+=v
    ld = nld
    #print(ld)

for i in range(40):
    step()

cnt = defaultdict(int)
for k,v in ld.items():
    cnt[k[0]] += v
    cnt[k[1]] += v
cnt[l[0]]+=1
cnt[l[-1]]+=1
cnts = sorted(cnt.values())
print((cnts[-1] - cnts[0]) / 2)