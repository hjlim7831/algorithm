import sys
input = sys.stdin.readline

N = int(input())

def hanoii(st, ed, N):
    mid = 6 - st - ed
    if N == 1:
        print(st, ed)
        return
    hanoii(st, mid, N-1)
    print(st, ed)
    hanoii(mid, ed, N-1)

print(2**N-1)
hanoii(1, 3, N)