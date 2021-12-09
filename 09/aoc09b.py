import sys
from collections import defaultdict
from itertools import chain

ls = sys.stdin.readlines()
m = [[int(e) for e in l.strip()] for l in ls]
M = len(m)
N = len(m[0])

def main():
    ret = 0
    for j in range(M):
        for i in range(N):
            if ((j+1 == M or m[j][i] < m[j+1][i]) and
               (j == 0 or m[j][i] < m[j-1][i]) and
               (i+1 == N or m[j][i] < m[j][i+1]) and
               (i == 0 or m[j][i] < m[j][i-1])):
                ret+=m[j][i]+1
    print(ret)

main()
