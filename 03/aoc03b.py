import sys
from collections import defaultdict

ls = [l.strip() for l in sys.stdin.readlines()]
W = len(ls[0])

def msb(ls, i):
    d = defaultdict(list)
    for l in ls:
        d[l[i]].append(l)
    if len(d['0']) > len(d['1']):
        return d['0']
    else:
        return d['1']

def lsb(ls, i):
    d = defaultdict(list)
    for l in ls:
        d[l[i]].append(l)
    if len(d['0']) == len(ls) or (len(d['0']) > 0 and len(d['0']) <= len(d['1'])):
        return d['0']
    else:
        return d['1']


def toint(b):
    ret = 0
    for i, c in enumerate(b):
        if c == '1':
            ret |= (1<<(W-1-i))
    return ret

cur = ls
for i in range(0, W):
    cur = msb(cur, i)
gamma = toint(cur[0])

cur = ls
for i in range(0, W):
    cur = lsb(cur, i)
eps = toint(cur[0])

print(f'gamma: {gamma} eps: {eps} result: {gamma*eps}')
