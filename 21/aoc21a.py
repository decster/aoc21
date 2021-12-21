import sys

ls = [e.strip() for e in sys.stdin.readlines()]
pos = [int(ls[0][-1])-1, int(ls[1][-1])-1]
score = [0, 0]

print(pos)

ndice = 0
dicev = 0
p = 0
while True:
    ndice+=3
    v = 3 + dicev
    dicev = (dicev + 1) % 100
    v += dicev
    dicev = (dicev + 1) % 100
    v += dicev
    dicev = (dicev + 1) % 100
    pos[p] = (pos[p] + v) % 10
    score[p] += pos[p] + 1
    print(f'score[{p}] = {score[p]}')
    np = (p + 1) % 2
    if score[p] >= 1000:
        print(f'{score[np]}*{ndice}={score[np]*ndice}')
        break
    p = np
