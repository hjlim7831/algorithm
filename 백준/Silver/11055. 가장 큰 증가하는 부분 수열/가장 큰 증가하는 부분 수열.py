import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = A[:]

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

# print(dp)
print(max(dp))