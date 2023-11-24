import sys
input = sys.stdin.readline

n = int(input())

score_a, score_b = 100, 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        score_b -= a
    elif a < b:
        score_a -= b

print(score_a)
print(score_b)