import sys
from collections import defaultdict


ls = sys.stdin.readlines()
ns = [int(e) for e in ls[0].split(',')]

#DAY = 80
DAY = 256

def main():
    all = [0] * 9
    for n in ns:
        all[n]+=1
    for day in range(DAY):
        newall = [0] * 9
        for i in range(1, 9):
            newall[i-1] = all[i]
        newall[6] += all[0]
        newall[8] = all[0]
        all = newall
        print(all)
    print(sum(all))

main()
