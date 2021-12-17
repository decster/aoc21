import sys
from collections import defaultdict
from itertools import chain
from queue import PriorityQueue

m = [[int(c) for c in e.strip()] for e in sys.stdin.readlines()]
N = len(m)
mark = [[False]*N  for e in range(N)]
dis = [[2000000000]*N for e in range(N)]

dis[0][0] = 0
mark[0][0] = True
cur = (0,0)
ds = [(-1,0), (1,0), (0,-1), (0, 1)]


def pdis():
    for i in range(N):
        print(' '.join(str(e) for e in dis[i]))
    print(f'--------------- {cur}')


while True:
    for e in ds:
        p = (cur[0] + e[0], cur[1] + e[1])
        if 0 <= p[0] < N and 0 <= p[1] < N:
            dis[p[0]][p[1]] = min(dis[p[0]][p[1]], dis[cur[0]][cur[1]] + m[p[0]][p[1]])
    minpos = None
    minv = None
    for i in range(N):
        for j in range(N):
            if not mark[i][j] and (minpos is None or dis[i][j] < minv):
                minv = dis[i][j]
                minpos = (i, j)
    if minpos == (N-1, N-1):
        print(minv)
        break
    mark[minpos[0]][minpos[1]] = True
    cur = minpos
    #pdis()
