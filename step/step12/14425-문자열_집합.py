N, M = map(int,input().split())
S = set()
for i in range(N):
    S.add(input())

ans = 0
for i in range(M):
    det = input()
    if det in S:
        ans += 1

print(ans)