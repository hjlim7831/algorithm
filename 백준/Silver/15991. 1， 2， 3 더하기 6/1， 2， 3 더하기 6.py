import sys
input = sys.stdin.readline

DIV = 1_000_000_009
RANGE1 = 50_001
RANGE2 = 100_001

dp1 = [0] * RANGE1
dp1[1] = 1
dp1[2] = 2 # 2 = 1 + 1
dp1[3] = 4 # 3 = 1 + 2 = 2 + 1 = 1 + 1 + 1

for i in range(4, RANGE1):
    dp1[i] = (dp1[i-1] + dp1[i-2] + dp1[i-3]) % DIV

dp2 = [0] * RANGE2
dp2[1] = 1 # 1
dp2[2] = 2 # 2 = 1 + 1
dp2[3] = 2 # 3 = 1 + 1 + 1
for i in range(4, RANGE2):
    if i % 2 == 0:
        dp2[i] = (dp1[i//2] + dp1[(i-2)//2]) % DIV
    else:
        dp2[i] = (dp1[(i-1)//2] + dp1[(i-3)//2]) % DIV

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp2[n])