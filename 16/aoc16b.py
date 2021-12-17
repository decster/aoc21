import sys
from collections import defaultdict
from itertools import chain
import functools
from queue import PriorityQueue

if len(sys.argv) == 2:
    m = sys.argv[1]
else:
    m = sys.stdin.readlines()[0].strip()

print(m)

def hex(c):
    if ord(c) >= ord('A'):
        return ord(c) - ord('A') + 10
    else:
        return ord(c) - ord('0')

b = ''.join('{0:04b}'.format(hex(c)) for c in m)
print(b)

def num(b):
    return int(b, 2)


vsum = 0

def parse(b):
    #print(f'parse {b}')
    global vsum
    vvv = num(b[:3])
    vsum += vvv
    ttt = num(b[3:6])
    if ttt == 4:
        ci = 6
        v = 0
        while True:
            v = (v << 4) + num(b[ci+1:ci+5])
            if b[ci] == '0':
                break
            ci+=5
        ci+=5
        return ci, v
    else:
        # parse op
        I = num(b[6:7])
        vs = []
        if I == 0:
            # length 15
            splen = num(b[7:22])
            ci = 22
            while ci < 22 + splen:
                r1, r2 = parse(b[ci:22+splen])
                ci += r1
                vs.append(r2)
            reti = 22 + splen
        else:
            # length 11
            nsp = num(b[7:18])
            ci = 18
            for pi in range(nsp):
                r1, r2 = parse(b[ci:])
                ci += r1
                vs.append(r2)
            reti = ci
        if ttt == 0:
            v = sum(vs)
        elif ttt == 1:
            v = functools.reduce(lambda a,b:a*b, vs)
        elif ttt == 2:
            v = min(vs)
        elif ttt == 3:
            v = max(vs)
        elif ttt == 5:
            v = 1 if vs[0] > vs[1] else 0
        elif ttt == 6:
            v = 1 if vs[0] < vs[1] else 0
        elif ttt == 7:
            v = 1 if vs[0] == vs[1] else 0
        else:
            raise Exception('bad op')
        return reti, v


print(parse(b)[1])
