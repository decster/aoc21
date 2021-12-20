import sys

ls = [e.strip() for e in sys.stdin.readlines()]
d = [0 if c == '.' else 1 for c in ls[0]]
m = [[0 if c == '.' else 1 for c in l] for l in ls[2:]]
o = 0 # outside region color

ps = (
    (0,0),(0,-1),(0,-2),
    (-1,0),(-1,-1),(-1,-2),
    (-2,0),(-2,-1),(-2,-2),
)

def step(m, o):
    M = len(m)
    N = len(m[0])
    ret = [[0]*(N+2) for i in range(M+2)]
    for i in range(M+2):
        for j in range(N+2):
            idx = 0
            for s, p in enumerate(ps):
                di = i + p[0]
                dj = j + p[1]
                inside = 0 <= di < M and 0 <= dj < N
                if inside and m[di][dj] or not inside and o == 1:
                    idx += 1 << s
            ret[i][j] = d[idx]
    return ret, d[0] if o == 0 else d[511]

def printm(m):
    for l in m:
        print(''.join('#' if c == 1 else '.' for c in l))
    print()

for i in range(50):
    m, o = step(m, o)
    if i in (1, 49):
        print(sum(sum(e) for e in m))
