import sys
from collections import defaultdict
from itertools import chain
import heapq

sm = [[int(c) for c in e.strip()] for e in sys.stdin.readlines()]
SN = len(sm)
N = SN * 5
m = [[0]*N for e in range(N)]
for i in range(N):
    for j in range(N):
        m[i][j] = (sm[i%SN][j%SN] - 1 + i//SN + j//SN) % 9 + 1
mark = [[False]*N  for e in range(N)]


def pmap(cur):
    for i in range(N):
        for j in range(N):
            if (i,j) == cur:
                print(f'\033[93m{m[i][j]}\033[0m', end='')
            else:
                print(m[i][j], end='')
        print()
    print()


heap = [(0, (0,0))]
while heap:
    dis, cur = heapq.heappop(heap)
    if mark[cur[0]][cur[1]]:
        continue
    if cur == (N-1, N-1):
        print(dis)
        break
    mark[cur[0]][cur[1]] = True
    for e in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        p = (cur[0] + e[0], cur[1] + e[1])
        if 0 <= p[0] < N and 0 <= p[1] < N and not mark[p[0]][p[1]]:
            heapq.heappush(heap, (dis + m[p[0]][p[1]], p))
