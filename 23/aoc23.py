import sys
from collections import defaultdict
import heapq

#start = ((None,None,None,None,None,None,None),((1,3,3,0),(2,2,1,3),(1,1,0,2),(3,0,2,0)))
start = ((None,None,None,None,None,None,None),((3,3,3,3),(1,2,1,0),(2,1,0,1),(2,0,2,0)))
goal = ((None,None,None,None,None,None,None),((0,0,0,0),(1,1,1,1),(2,2,2,2),(3,3,3,3)))

checkslots = [
    (((1,2),(0,3)), ((2,2),(3,4),(4,6),(5,8),(6,9))),
    (((2,2),(1,4),(0,5)), ((3,2),(4,4),(5,6),(6,7))),
    (((3,2),(2,4),(1,6),(0,7)), ((4,2),(5,4),(6,5))),
    (((4,2),(3,4),(2,6),(1,8),(0,9)), ((5,2),(6,3))),
]
iscores = (1,10,100,1000)



def pstate(state, score):
    chars = 'ABCD'
    slots, rooms = state
    cslots = ['.' if e is None else chars[e] for e in slots]
    print(f"{cslots[0]}{'.'.join(cslots[1:6])}{cslots[6]}")
    m = [['.'] * 11 for e in range(4)]
    for i,room in enumerate(rooms):
        for h,c in enumerate(room):
            m[4-len(room)+h][2+i*2] = chars[c]
    print('\n'.join(''.join(l) for l in m))
    print(f' score: {score}\n          ')

def availble_slots(slots, i):
    lc, rc = checkslots[i]
    ret = []
    for e in lc:
        if slots[e[0]] is None:
            ret.append(e)
        else:
            break
    for e in rc:
        if slots[e[0]] is None:
            ret.append(e)
        else:
            break
    return ret

def try_put_back_1(state, score):
    slots, rooms = state
    for i,room in enumerate(rooms):
        if len(room) == 4:
            continue
        lc, rc = checkslots[i]
        for si,ds in lc:
            if slots[si] is None:
                continue
            if slots[si] == i and all(e == i for e in room):
                newslots = slots[:si] + (None,) + slots[si+1:]
                newrooms = rooms[:i] + ((i,) + room,) + rooms[i+1:]
                newscore = score + (ds + 3 - len(room)) * iscores[i]
                return (newslots, newrooms), newscore
            break
        for si,ds in rc:
            if slots[si] is None:
                continue
            if slots[si] == i and all(e == i for e in room):
                newslots = slots[:si] + (None,) + slots[si+1:]
                newrooms = rooms[:i] + ((i,) + room,) + rooms[i+1:]
                newscore = score + (ds + 3 - len(room)) * iscores[i]
                return (newslots, newrooms), newscore
            break
    return None, None


def try_put_back(state, score):
    while True:
        newstate, newscore = try_put_back_1(state, score)
        if newstate is None:
            return state, score
        state, score = newstate, newscore



class HeapEntry(object):
    def __init__(self, score, state, pre):
        self.score = score
        self.state = state
        self.pre = pre
    def __lt__(self, o):
        return self.score < o.score

marked = dict()
q = [HeapEntry(0,start,None)]

while q:
    he = heapq.heappop(q)
    score, cur = he.score, he.state
    if cur in marked:
        continue
    #pstate(cur, score)
    marked[cur] = he.pre
    if cur == goal:
        hist = [he]
        while hist[-1].state != start:
            hist.append(marked[hist[-1].state])
        for e in reversed(hist):
            pstate(e.state, e.score)
        break
    slots, rooms = cur
    for i,room in enumerate(rooms):
        if all(e == i for e in room):
            continue
        aslots = availble_slots(slots, i)
        for ci,ds in aslots:
            newslots = slots[:ci] + (room[0],) + slots[ci+1:]
            newrooms = rooms[:i] + (room[1:],) + rooms[i+1:]
            newscore = score + (ds + 4 - len(room)) * iscores[room[0]]
            newstate = (newslots, newrooms)
            newstate, newscore = try_put_back(newstate, newscore)
            if newstate in marked:
                continue
            heapq.heappush(q, HeapEntry(newscore, newstate, he))


