import sys
from collections import defaultdict


ls = sys.stdin.readlines()
dps = [l.split(' | ') for l in ls]
ds = [s[0].split() for s in dps]
ps = [s[1].split() for s in dps]

def main():
    ret = 0
    for p in ps:
        ret += sum(len(e) in (2,3,4,7) for e in p)
    print(ret)

main()
