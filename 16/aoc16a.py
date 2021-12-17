import sys
from collections import defaultdict
from itertools import chain
from queue import PriorityQueue

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
        while True:
            if b[ci] == '0':
                break
            ci+=5
        ci+=5
        return ci
    else:
        # parse op
        I = num(b[6:7])
        if I == 0:
            # length 15
            splen = num(b[7:22])
            ci = 22
            while ci < 22 + splen:
                ci += parse(b[ci:22+splen])
            return 22 + splen
        else:
            # length 11
            nsp = num(b[7:18])
            ci = 18
            for pi in range(nsp):
                ci += parse(b[ci:])
            return ci

parse(b)
print(vsum)