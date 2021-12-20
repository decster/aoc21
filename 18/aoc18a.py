import sys
import math
import json

class NS(object):
    def __init__(self, l, parent=None):
        self.parent = parent
        if isinstance(l, list):
            self.v = None
            if isinstance(l[0], NS):
                self.l = l[0]
                l[0].parent = self
            else:
                self.l = NS(l[0], self)
            if isinstance(l[1], NS):
                self.r = l[1]
                l[1].parent = self
            else:
                self.r = NS(l[1], self)
        else:
            self.v = l
            self.l = None
            self.r = None
    def reset0(self):
        self.v = 0
        self.l = None
        self.r = None
    def leaves(self):
        if self.v is None:
            for e in self.l.leaves():
                yield e
            for e in self.r.leaves():
                yield e
        else:
            yield self
    def depth(self):
        return 0 if self.parent is None else 1 + self.parent.depth()
    def explode(self):
        vs = list(self.leaves())
        for i in range(len(vs)):
            if vs[i].depth() == 5:
                if i >= 1:
                    vs[i-1].v += vs[i].v
                if i + 2 < len(vs):
                    vs[i+2].v += vs[i+1].v
                vs[i].parent.reset0()
                return True
        return False
    def split(self):
        for e in self.leaves():
            if e.v >= 10:
                e.l = NS(math.floor(e.v/2), e)
                e.r = NS(math.ceil(e.v/2), e)
                e.v = None
                return True
        return False
    def reduce(self):
        while True:
            if self.explode():
                continue
            if self.split():
                continue
            break
    def __add__(self, rhs):
        ret = NS([self, rhs])
        ret.reduce()
        return ret
    def mag(self):
        return self.v if isinstance(self.v, int) else 3 * self.l.mag() + 2 * self.r.mag()


ls = [json.loads(e) for e in sys.stdin.readlines()]

def sum_mag():
    nss = [NS(e) for e in ls]
    s = nss[0]
    for i in range(1, len(nss)):
        s = s + nss[i]
    print(s.mag())

def maxmag():
    mmag = 0
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j:
                mmag = max(mmag, (NS(ls[i]) + NS(ls[j])).mag())
    print(mmag)

maxmag()
