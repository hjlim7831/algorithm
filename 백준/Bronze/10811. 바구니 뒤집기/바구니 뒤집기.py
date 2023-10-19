import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    st, ed = map(int, input().split())
    tmp = basket[st-1:ed][::-1]
    for i in range(ed-st+1):
        basket[i+st-1] = tmp[i]

print(*basket)
