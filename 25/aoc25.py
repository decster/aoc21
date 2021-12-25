import sys
import copy

s = [list(l.strip()) for l in sys.stdin.readlines()]
M = len(s)
N = len(s[0])


def step():
    global s
    ok = True
    ns = copy.deepcopy(s)
    for i in range(M):
        for j in range(N):
            if s[i][j] == '>' and s[i][(j+1) % N] == '.':
                ns[i][(j+1) % N] = '>'
                ns[i][j] = '.'
                ok = False
    s = ns
    ns = copy.deepcopy(s)
    for i in range(M):
        for j in range(N):
            if s[i][j] == 'v' and s[(i+1) % M][j] == '.':
                ns[(i+1) % M][j] = 'v'
                ns[i][j] = '.'
                ok = False
    s = ns
    return ok

st = 0
while True:
    st += 1
    if step():
        break
print(st)
