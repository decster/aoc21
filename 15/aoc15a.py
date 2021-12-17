import sys
from collections import defaultdict
from itertools import chain
from queue import PriorityQueue

m = [[int(c) for c in e.strip()] for e in sys.stdin.readlines()]

for l in m:
    print(l)
