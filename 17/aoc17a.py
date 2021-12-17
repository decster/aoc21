import sys
from collections import defaultdict
from itertools import chain
from queue import PriorityQueue

fs = [e.strip() for e in sys.stdin.readlines()][0].split(' ')
rx = fs[2][2:-1].split('..')
rx = (int(rx[0]), int(rx[1]))
ry = fs[3][2:].split('..')
ry = (int(ry[0]), int(ry[1]))

def dx(vx):
    return (vx + 1) * vx // 2


def minx(dis):
    for i in range(dis+1):
        if dx(i) >= dis:
            return i

print(f'{rx} {ry}')

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def run(v, rx, ry):
    pos = (0, 0)
    h = 0
    while True:
        pos = (pos[0] + v[0], pos[1] + v[1])
        h = max(h, pos[1])
        if rx[0] <= pos[0] <= rx[1] and ry[0] <= pos[1] <= ry[1]:
            return h
        v = (v[0] - sign(v[0]), v[1] - 1)
        if (v[0] == 0 and pos[0] < rx[0]) or (v[1] < 0 and pos[1] < ry[0]) or (pos[0] > rx[1]):
            return None

mx = ry[0]

for tx in range(minx(rx[0]), rx[1]+1):
    for ty in range(0, abs(ry[0])):
        h = run((tx, ty), rx, ry)
        if h is not None:
            mx = max(mx, h)

print(mx)