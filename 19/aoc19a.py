from itertools import combinations, product
import sys
from collections import defaultdict

def psub(p1,p2): return p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2]
def padd(p1,p2): return p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2]
def rotate(s,R): return (R[0]*s[R[3]],R[1]*s[R[4]],R[2]*s[R[5]])
def rt(s, RT): return padd(rotate(s, RT[0]), RT[1])

rs  = ([(a,b,c,i,j,k) for a,b,c in [(1,1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1)] for i,j,k in [(2,1,0),(1,0,2),(0,2,1)]]
      +[(a,b,c,i,j,k) for a,b,c in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)] for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]])

ss = [[eval(line) for line in scanner.splitlines() if '--' not in line]
            for scanner in sys.stdin.read().split('\n\n')]

N = len(ss)
RTs = {}
RTs[0] = [((0,0,0,0,1,2), (0,0,0)), False, 0]
all = set(ss[0])

def to0(i, p):
    while i != 0:
        p = rt(p, RTs[i][0])
        i = RTs[i][2]
    return p


def dists(ps):
    ret = defaultdict(list)
    for i in range(len(ps)):
        for j in range(len(ps)):
            if i != j:
                ret[psub(ps[i], ps[j])].append((ps[i], ps[j]))
    return ret


def match(s, d):
    # return RT
    sds = dists(s)
    dds = dists(d)
    for r in rs:
        nmatch = 0
        tset = defaultdict(int)
        for d,dn in dds.items():
            rd = rotate(d, r)
            if rd in sds:
                nmatch += min(len(dn), len(sds[rd]))
                if len(dn) == 1 and len(sds[rd]) == 1:
                    t = psub(sds[rd][0][0], rotate(dn[0][0], r))
                    tset[t]+=1
        if nmatch >= 12 * 11:
            # t is transform with largest support
            t = sorted((v,k) for k,v in tset.items())[-1][1]
            return (r, t)


while len(RTs) < N:
    for k,v in list(RTs.items()):
        if not v[1]:
            for i in range(N):
                if i not in RTs:
                    ret = match(ss[k], ss[i])
                    if ret:
                        print(f'match {k} {i}')
                        RTs[i] = [ret, False, k]
                        for p in ss[i]:
                            all.add(to0(i, p))
            v[1] = True

print(f'{len(all)}')

def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

sposes = [to0(i, (0,0,0)) for i in range(N)]

print('max mnhattan: ', max(manhattan(p0, p1) for p0, p1 in combinations(sposes, 2)))
