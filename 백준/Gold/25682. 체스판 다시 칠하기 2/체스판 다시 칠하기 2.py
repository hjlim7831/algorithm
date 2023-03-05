import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [" "*(M+1)]

for _ in range(N):
    board.append(" "+input().rstrip())

# BWBWBW.. 형태로 2차원 누적합 구하기
# WBWBWB.. 
acc = [[0]*(M+1) for _ in range(N+1)]

det = ["B", "W"]

for i in range(1, N+1):
    for j in range(1, M+1):
        now = acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1]
        if board[i][j] == det[(i+j)%2]:
            now += 1
        acc[i][j] = now

min_chg = K * K

for i in range(K, N+1):
    for j in range(K, M+1):
        tmp_chg = acc[i][j] - acc[i][j-K] - acc[i-K][j] + acc[i-K][j-K]
        min_chg = min(tmp_chg, K * K - tmp_chg, min_chg)

print(min_chg)