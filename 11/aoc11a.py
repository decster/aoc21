import sys
from collections import defaultdict
from itertools import chain

ls = [e.strip() for e in sys.stdin.readlines()]
m = [[int(e) for e in l] for l in ls]

nbs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]


def p():
    for i in range(10):
        for j in range(10):
            print(m[i][j], end='')
        print()
    print()


def step():
    q = []
    for i in range(10):
        for j in range(10):
            m[i][j]+=1
            if m[i][j] > 9:
                q.append((i,j))
    while len(q) > 0:
        nq = []
        for i,j in q:
            for nb in nbs:
                ny, nx = i+nb[0], j+nb[1]
                if 0 <= ny < 10 and 0 <= nx < 10 and m[ny][nx] <= 9:
                    m[ny][nx] += 1
                    if m[ny][nx] == 10:
                        nq.append((ny, nx))
        q = nq
    ret = 0
    for i in range(10):
        for j in range(10):
            if m[i][j] == 10:
                ret+=1
                m[i][j] = 0
    return ret


def main():
    ret = 0
    for s in range(1000):
        if step() == 100:
            print(f'step: {s+1}')
            return

main()
