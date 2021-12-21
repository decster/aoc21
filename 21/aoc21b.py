import sys
from collections import defaultdict

ls = [e.strip() for e in sys.stdin.readlines()]
pos = [int(ls[0][-1])-1, int(ls[1][-1])-1]
print(pos)

# state = (score0, score1, pos0, pos1)
states = defaultdict(int)
states[(0, 0, pos[0], pos[1])] += 1

vdice = [0] * 10
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            vdice[i+j+k] += 1

wins = [0,0]
p = 0
while len(states) > 0:
    print(f'player {p}: #state: {len(states)}')
    nstates = defaultdict(int)
    if p == 0:
        for k,v in states.items():
            s0, s1, pos0, pos1 = k
            for dv in range(3,10):
                npos0 = (pos0 + dv) % 10
                ns0 = s0 + npos0 + 1
                if ns0 >= 21:
                    wins[p] += v * vdice[dv]
                else:
                    nstates[(ns0, s1, npos0, pos1)] += v * vdice[dv]
    else:
        for k,v in states.items():
            s0, s1, pos0, pos1 = k
            for dv in range(3,10):
                npos1 = (pos1 + dv) % 10
                ns1 = s1 + npos1 + 1
                if ns1 >= 21:
                    wins[p] += v * vdice[dv]
                else:
                    nstates[(s0, ns1, pos0, npos1)] += v * vdice[dv]
    p = (p + 1) % 2
    states = nstates

print(wins)
