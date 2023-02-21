import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [i for i in range(1, N + 1)]

for _ in range(M):
    # print(basket)
    begin, end, mid = map(int, input().split())
    # print(begin, end, mid)
    bidx, eidx, midx = begin -1, end -1, mid -1
    basket = basket[:bidx] +basket[midx:eidx+1] + basket[bidx:midx] + basket[eidx+1:]

print(*basket)