import sys
from collections import defaultdict


ls = [l.strip() for l in sys.stdin.readlines()]
N = (len(ls) - 1) // 6

ns = [int(e) for e in ls[0].split(',')]

boards = []
for i in range(N):
    b = [[[int(e),False] for e in l.split()] for l in ls[2+i*6: 2+i*6+5]]
    boards.append(b)

def p(b):
    for i in range(5):
        for j in range(5):
            print('% 3d %d' % (b[i][j][0], 1 if b[i][j][1] else 0), end='')
        print()
    print()

def mark(b, v):
    for i in range(5):
        for j in range(5):
            if b[i][j][0] == v:
                b[i][j][1] = True
                return True
    return False

def win(b):
    for i in range(5):
        if all(e[1] for e in b[i]):
            return True
        if all(e[i][1] for e in b):
            return True
    return False


def main():
    for v in ns:
        print(f'update: {v}')
        for b in boards:
            if mark(b, v):
                p(b)
                if win(b):
                    s = 0
                    for i in range(5):
                        for j in range(5):
                            if b[i][j][1] == False:
                                s+=b[i][j][0]
                    print(s)
                    print(s*v)
                    return

main()
