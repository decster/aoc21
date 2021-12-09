import sys
from collections import defaultdict
from itertools import chain

ls = sys.stdin.readlines()
m = [[int(e) for e in l.strip()] for l in ls]
M = len(m)
N = len(m[0])
mark = [[0]*N for i in range(M)]

cnt = 0

def dfs(j, i):
    if mark[j][i] == 1 or m[j][i] == 9:
        return
    mark[j][i] = 1
    global cnt
    cnt+=1
    if i > 0:
        dfs(j, i-1)
    if j > 0:
        dfs(j-1, i)
    if i + 1 < N:
        dfs(j, i+1)
    if j + 1 < M:
        dfs(j+1, i)


def main():
    ms = []
    global cnt
    for j in range(M):
        for i in range(N):
            cnt = 0
            dfs(j,i)
            if cnt > 0:
                ms.append(cnt)
    ms.sort(reverse=True)
    print(ms[0]*ms[1]*ms[2])

main()
