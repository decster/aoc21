import sys
from collections import defaultdict


v0 = [ 1, 1, 1,26, 1, 26, 1, 26, 1, 1, 26, 26, 26, 26]
v1 = [13,12,11, 0,15,-13,10, -9,11,13,-14, -3, -2,-14]
v2 = [14, 8, 5, 4,10, 13,16,  5, 6,13,  6,  7, 13,  3]

# program
# if z%26 + v1 != w:
#     z /= v0
#     z *= 26
#     z += w + v2
# else:
#     z /= v0

wc = list(range(9,0,-1))

def dfs(i, z, st):
    if i == 14:
        if z == 0:
            print(st)
            return True
        else:
            return False
    ifz = z % 26 + v1[i]
    candi = [ifz] if 1 <= ifz <= 9 else wc
    for w in candi:
        nz = (z // v0[i] * 26) + w + v2[i] if w != ifz else z // v0[i]
        if nz >= 26**4:
            continue
        st.append(w)
        if dfs(i+1, nz, st):
            return True
        st.pop()
    return False

dfs(0,0,[])

wc_min = list(range(1,10))

def dfs_min(i, z, st):
    if i == 14:
        if z == 0:
            print(st)
            return True
        else:
            return False
    ifz = z % 26 + v1[i]
    candi = [ifz] if 1 <= ifz <= 9 else wc_min
    for w in candi:
        nz = (z // v0[i] * 26) + w + v2[i] if w != ifz else z // v0[i]
        if nz >= 26**4:
            continue
        st.append(w)
        if dfs_min(i+1, nz, st):
            return True
        st.pop()
    return False

dfs_min(0,0,[])

#
# ls = [e.strip() for e in sys.stdin.readlines()]
# MN = '99999999999999'
#
# def check(p, mn):
#     i = 0
#     state = {'x':0, 'y':0, 'z':0, 'w':0}
#     def getv(op):
#         if op in 'xyzw':
#             return state[op]
#         else:
#             return int(op)
#     for ist in ls:
#         cmd = ist[:3]
#         if cmd == 'inp':
#             state['w'] = int(mn[i])
#             i+=1
#         elif cmd == 'add':
#             a = ist[4]
#             b = getv(ist[6:])
#             state[a] += b
#         elif cmd == 'mul':
#             a = ist[4]
#             b = getv(ist[6:])
#             state[a] = state[a] * b
#         elif cmd == 'div':
#             a = ist[4]
#             b = getv(ist[6:])
#             state[a] = state[a]//b
#         elif cmd == 'mod':
#             a = ist[4]
#             b = getv(ist[6:])
#             state[a] = state[a] % b
#         elif cmd == 'eql':
#             a = ist[4]
#             b = getv(ist[6:])
#             state[a] = 1 if state[a] == b else 0
#         else:
#             raise Exception('int illegal')
#         print(f'{mn}: {state}')
#     if state['z'] == 10:
#         return True
#     return False

# for i in range(1000000):
#     mn = str(88999999999999 - i)
#     if check(ls, mn):
#         break
