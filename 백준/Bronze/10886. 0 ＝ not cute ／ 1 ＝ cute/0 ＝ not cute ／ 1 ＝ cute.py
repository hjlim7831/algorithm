import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    ans += int(input())

if ans > N - ans:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")