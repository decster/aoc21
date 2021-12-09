import sys
from collections import defaultdict


ls = [[[int(v) for v in e.split(',')] for e in l.strip().split(' -> ')] for l in sys.stdin.readlines()]


def main():
    all = defaultdict(int)
    for s in ls:
        if s[0][0] == s[1][0]:
            vmin = min(s[0][1], s[1][1])
            vmax = max(s[0][1], s[1][1])
            for y in range(vmin, vmax+1):
                all[y*10000 + s[0][0]]+=1
        elif s[0][1] == s[1][1]:
            vmin = min(s[0][0], s[1][0])
            vmax = max(s[0][0], s[1][0])
            for x in range(vmin, vmax+1):
                all[s[0][1]*10000 + x]+=1
        elif abs(s[0][1] - s[1][1]) == abs(s[0][0] - s[1][0]):
            d = abs(s[0][1] - s[1][1])
            for i in range(d+1):
                x = s[0][0] + (s[1][0] - s[0][0])//d * i
                y = s[0][1] + (s[1][1] - s[0][1])//d * i
                all[y*10000 + x]+=1
    ret = 0
    for v in all.values():
        if v > 1:
            ret+=1
    print(ret)

main()
