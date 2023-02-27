import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def comb(sidx:int, idx:int, res:list):
    global N, M
    if sidx == M:
        print(*res)
        return
    if idx == N:
        return
    res.append(idx+1)
    comb(sidx+1, idx+1, res)
    res.remove(res[-1])
    comb(sidx, idx+1, res)

comb(0, 0, [])