import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
is_pelindrome = [[False]*N for _ in range(N)]

for S in range(N):
    is_pelindrome[S][S] = True

for S in range(N-1):
    E = S+1
    if numbers[S] == numbers[E]:
        is_pelindrome[S][E] = True


for l in range(3, N+1):
    for S in range(N-l+1):
        E = S + l - 1
        # print(S, E)
        if is_pelindrome[S+1][E-1] and numbers[S] == numbers[E]:
            is_pelindrome[S][E] = True
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if is_pelindrome[S-1][E-1]:
        print(1)
    else:
        print(0)