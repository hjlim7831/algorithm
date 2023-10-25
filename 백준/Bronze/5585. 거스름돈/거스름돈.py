import sys
input = sys.stdin.readline

rest = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]

ans = 0
for c in coins:
    ans += rest // c
    rest = rest % c

print(ans)

