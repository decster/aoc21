import sys
from collections import defaultdict
from itertools import chain

pts = set()

def print_pts():
    mm = [[' ']*20 for e in range(80)]
    for pt in pts:
        mm[pt[1]][pt[0]] = '*'
    for l in mm:
        print(''.join(l))

def fold(d, p):
    p = int(p)
    global pts
    newpts = set()
    for pt in pts:
        if d == 'y':
            newpts.add((pt[0], pt[1] if pt[1] < p else p - (pt[1] - p)))
        else:
            newpts.add((pt[0] if pt[0] < p else p - (pt[0] - p), pt[1]))
    pts = newpts
    print(len(pts))

for e in sys.stdin.readlines():
    if e[0] == 'f':
        fold(*e.split(' ')[2].split('='))
    elif len(e) > 1:
        d = e.split(',')
        pts.add((int(d[0]), int(d[1])))

print_pts()