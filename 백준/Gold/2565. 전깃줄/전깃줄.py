import sys
input = sys.stdin.readline

N = int(input())
pos = []

for _ in range(N):
    pos.append(tuple(map(int, input().split())))

# 우선 한 개의 전봇대 기준으로 sort
pos.sort(key=lambda x: x[0])


# 다른 전봇대에서 최장 증가수열 찾기
dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if pos[i][1] > pos[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# 없애야 하는 전깃줄의 최소 개수 출력
print(N - max(dp))