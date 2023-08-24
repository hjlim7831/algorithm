import sys, math
from collections import deque
from itertools import permutations
input = sys.stdin.readline

N = int(input())
LARGE_NUMBER = 100


if N == 1:
    hp = int(input())
    ans = int(math.ceil(hp/9))

elif N == 2:
    hp1, hp2 = map(int, input().split())
    dp = [[LARGE_NUMBER] * (hp2+1) for _ in range(hp1+1)]
    dp[hp1][hp2] = 0
    que = deque([(hp1, hp2)])
    while que:
        hp1, hp2 = que.popleft()
        for n1, n2 in permutations([9, 3], 2):
            # print(n1, n2)
            np1 = max(hp1 - n1, 0)
            np2 = max(hp2 - n2, 0)
            if dp[np1][np2] > dp[hp1][hp2] + 1:
                dp[np1][np2] = dp[hp1][hp2] + 1
                que.append((np1, np2))
    ans = dp[0][0]
else:
    hp1, hp2, hp3 = map(int, input().split())
    dp = [[[LARGE_NUMBER] * (hp3+1) for _ in range(hp2+1)] for _ in range(hp1+1)]
    dp[hp1][hp2][hp3] = 0
    que = deque([(hp1, hp2, hp3)])
    while que:
        hp1, hp2, hp3 = que.popleft()
        for n1, n2, n3 in permutations([9, 3, 1], 3):
            np1 = max(hp1 - n1, 0)
            np2 = max(hp2 - n2, 0)
            np3 = max(hp3 - n3, 0)
            if dp[np1][np2][np3] > dp[hp1][hp2][hp3] + 1:
                dp[np1][np2][np3] = dp[hp1][hp2][hp3] + 1
                que.append((np1, np2, np3))
    ans = dp[0][0][0]

print(ans)