import sys
from collections import defaultdict


ls = sys.stdin.readlines()
ns = [int(e) for e in ls[0].split(',')]

def main_a():
    newns = sorted(ns)
    mid = newns[len(newns)//2]
    ret = sum(abs(e - mid) for e in newns)
    print(ret)

def main_b():
    ret = 10000000000
    for mid in range(min(ns), max(ns)+1):
        cur = sum(abs(e - mid)*(abs(e-mid)+1)//2 for e in ns)
        if cur < ret:
            ret = cur
    print(ret)

main_b()
