import sys
from collections import defaultdict
from itertools import chain

ls = [e.strip() for e in sys.stdin.readlines()]

match = {
    '>' : '<',
    ']' : '[',
    '}' : '{',
    ')' : '('
}

score = {
    '>' : 25137,
    ']' : 57,
    '}' : 1197,
    ')' : 3
}


def gets(l):
    st = []
    for c in l:
        if c in ('<', '[', '{', '('):
            st.append(c)
        elif match[c] == st[-1]:
            st.pop()
        else:
            return score[c]
    return 0


def main():
    print(sum(gets(e) for e in ls))


main()
