import sys
from collections import defaultdict
from itertools import chain

ls = [e.strip() for e in sys.stdin.readlines()]

match = {
    '>': '<',
    ']': '[',
    '}': '{',
    ')': '('
}

score = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


cpls = []

def gets(l):
    st = []
    for c in l:
        if c in ('<', '[', '{', '('):
            st.append(c)
        elif match[c] == st[-1]:
            st.pop()
        else:
            return
    ret = 0
    for c in reversed(st):
        ret = ret * 5 + score[c]
    cpls.append(ret)

def main():
    for e in ls:
        gets(e)
    cpls.sort()
    print(cpls)
    print(cpls[len(cpls)/2])


main()
